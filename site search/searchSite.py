import requests
import time
import datetime
import csv
import os
import random

SEARCH_FOR = ['stocks and shares',
			'Stocks and Shares',
			'Stocks And Shares',
			'stocks & shares',
			'Stocks & Shares',
			'stocks &amp; shares',
			'Stocks &amp; Shares']

URL_LIST = 'urls.txt'

SPEED = 'medium' # 'slow', 'medium' (recommended) or 'fast'


def throttle(speed='medium'):
	if speed.lower() == 'fast':
		rate = range(1,100) # Avg. 0.5 seconds
	elif speed.lower() == 'medium':
		rate = range(1,250) # Avg. 1.25 seconds
	elif speed.lower() == 'slow':
		rate = range(250,500) # Avg. 3.75 seconds
	else:
		rate = rate = range(1,250) # Default to medium
	delay = float(random.choice(rate)) / 100
	time.sleep(delay)

def readURLs(url_file):
	with open(url_file, 'r') as f:
		url_list = f.readlines()
	return url_list

def findPhrase(phrase, html, limit=0):
	return html.count(phrase) > limit

def saveOutput(results):
	filename = '{}/resulsts_{}.csv'.format(os.path.dirname(os.path.realpath(__file__)), datetime.datetime.now().strftime('%Y-%m-%d'))
	with open(filename,'wb') as resultFile:
	    wr = csv.writer(resultFile, dialect='excel')
	    wr.writerows(results)
	return filename

def main():
	url_list = readURLs(URL_LIST)
	x = raw_input(' Searching {} URLs at "{}" speed setting.\n Press Enter to begin.\n'.format(len(url_list), SPEED))
	results = ['URL', 'SEARCH TERM', 'FOUND']
	x = 0
	for url in url_list:
		x = x + 1
		url = url.strip()
		if len(url) > 49:
			url_name = '...{}'.format(url[-50:])
		else:
			url_name = url
		print ' [{}/{}] Searching {}'.format(x, len(url_list), url_name)
		
		r = requests.get(url)
		html = r.text

		for phrase in SEARCH_FOR:
			found = findPhrase(phrase, html, limit=6)

			results.append([url, phrase, found])
			if found:
				print '	 [+] FOUND "{}"'.format(phrase)
		throttle(speed=SPEED)

	filename = saveOutput(results)
	print '\n Done. Saved results in {}'.format(filename)

if __name__ == '__main__':
	main()
	x = raw_input()