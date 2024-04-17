import urllib.request
import os
import json
def crawl(url):
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    filename = url.split('/')[-1]#去掉網址中的斜線，將他們分成一個個陣列並取最後一個值。如果最後的值沒有.json，就手動加入
    if not filename.endswith('.json'):
            filename += '.json'
    with open(filename, 'w') as file:
            file.write(json.dumps(data))
    print(data['data'])
crawl('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2')