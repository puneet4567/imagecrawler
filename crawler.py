import requests
from bs4 import BeautifulSoup
import json
import sys
import urllib.parse

def getdata(url):
    r = requests.get(url)
    return r.text

# Open the results file for writing
f = open("results.json", "w")

# Initialize the URL stack with the starting URL and depth
url_stack = []
results = []
max_depth = int(sys.argv[2])
url_stack.append({"url": sys.argv[1], "depth": 0})

# Main crawling loop
while len(url_stack) > 0:
    # Get the next URL from the stack
    current_url_info = url_stack.pop()
    try:
        # Fetch the HTML content of the page
        htmldata = getdata(current_url_info["url"])
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., connection errors, timeouts)
        print(f"Error fetching URL: {current_url_info['url']} - {e}")
        continue

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(htmldata, 'html.parser')

    # Extract image URLs
    for item in soup.find_all('img'):
        if 'src' in item.__dict__['attrs'] and item['src'] != "":
            new_object = {
                "imageUrl": item['src'],
                "sourceUrl": current_url_info["url"],
                "depth": current_url_info["depth"]
            }
            results.append(new_object)

    # Add links from the current page to the stack for further crawling
    if current_url_info["depth"] < max_depth:
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # Normalize the URL using urljoin to handle relative URLs
                absolute_url = urllib.parse.urljoin(current_url_info["url"], href)
                url_stack.append({"url": absolute_url, "depth": current_url_info["depth"] + 1})

# Write the results to a JSON file
json_object = json.dumps(results, indent=4)
f.write(json_object)
f.close()