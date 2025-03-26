# imagecrawler
Given a url, the crawler will scan the webpage for any images, and continue to every link inside that page and scan it as well.

CLI usage: 
        python3 crawler.py <start_url: string> <depth: number>

Example : python3 crawler.py https://www.google.com 1

Installing Requirements:

pip install -r requirements.txt


Description:

Given a url, the crawler will scan the webpage for any images, and continue to every link inside that page and scan it as well. 
The crawling should stop once <depth> is reached. depth=3 means we can go as deep as 3 pages from the source url (denoted by the < start_url > param), and depth=0 is just the first page. 

The crawler handles both absolute and relative URLs by normalizing them using `urllib.parse.urljoin`. This ensures that relative URLs are correctly resolved with respect to the base URL of the page. However, it may face challenges with JavaScript-heavy websites where links are generated dynamically, as it relies on parsing the initial HTML content.

Results are saved into a results.json file in the following format:
