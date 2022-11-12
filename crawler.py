import requests 
from bs4 import BeautifulSoup 
import json
import sys
   
def getdata(url): 
    r = requests.get(url) 
    return r.text 

f = open("results.json", "w") 

url_stack = []
results = []
max_depth = int(sys.argv[2])
url_stack.append({"url":sys.argv[1] , "depth":0})

while(len(url_stack) > 0):
    url_item = url_stack.pop()
    try:
        htmldata = getdata(url_item["url"] ) 
    except Exception as e:
        continue

    soup = BeautifulSoup(htmldata, 'html.parser') 
    
    for item in soup.find_all('img'):
        if 'src' in item.__dict__['attrs'] and item['src'] != "":
            new_object = {
                    "imageUrl": item['src'],
                    "sourceUrl": url_item["url"],
                    "depth": url_item["depth"]

            }
            results.append(new_object)

    if url_item["depth"] < max_depth :
        for link in soup.find_all('a'):
            url_stack.append({"url":link.get('href') , "depth": url_item["depth"] + 1})

json_object = json.dumps(results, indent=4)
f.write(json_object)
f.close()