import urllib.request

import json
def crawl(url):
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    return (data)
#crawl('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2')