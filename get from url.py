import requests


res=requests.get('https://www.youtube.com/')

with open('test.html', 'w',  encoding="utf-8") as t:
    t.write(res.text)

