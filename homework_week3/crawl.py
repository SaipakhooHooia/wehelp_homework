import urllib.request

import json
def crawl(url):
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    filename = url.split('/')[-1]
    if not filename.endswith('.json'):
            filename += '.json'
    with open(filename, 'w') as file:
            file.write(json.dumps(data))
    return (filename)
#crawl('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2')