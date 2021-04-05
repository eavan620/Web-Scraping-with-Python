# Download a picture and save it.

import requests
res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
picture = res.content
photo = open('/Users/eavan/Downloads/spider.png','wb')
photo.write(picture)
photo.close()

