# Download audio material.

import requests
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
sound = res.content
music = open('/Users/eavan/Downloads/music.mp3','wb')
music.write(sound)
music.close()

