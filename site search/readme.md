## Site Search

### Purpose
Given a list of URLs and a word or phrase, this script will find each occurrence of that phrase on each URL's page.

### Installation
**Requirements:**
- Python 2.7

**Installation**
- Download the contents of this directory
- Run `pip install -r requirements.txt`

### Usage
**Get URLs**
searchSite.py expects a text file with one complete URL per line. E.g.
```
https://www.mysite.com/
https://www.mysite.com/contact_us
https://www.mysite.com/contact_us/complaints
https://www.mysite.com/recommend-a-friend
```

Save this as `urls.txt` in the same folder as siteSearch.py

**List search terms**
siteSearch.py looms for *exact* matches, so open siteSearch.py and provide a list of terms that encompass all the spelling & capitalisation variations, e.g.:
```python
SEARCH_FOR = ['stocks and shares',
			'Stocks and Shares',
			'Stocks And Shares',
			'stocks & shares',
			'Stocks & Shares',
			'stocks &amp; shares',
			'Stocks &amp; Shares']
```

**Run**
Run the the script by double-clicking siteSearch.py or from the command prompt with the command `python siteSearch.py`.
