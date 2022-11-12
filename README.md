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

Results should be saved into a results.json file in the following format:
{
	results: [
		{
			imageUrl: string,
			sourceUrl: string // the page url this image was found on
			depth: number // the depth of the source at which this image was found on
		}
	]
}

Web crawler introduction can be found here: https://en.wikipedia.org/wiki/Web_crawler
