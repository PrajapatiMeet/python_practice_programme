import urllib.request
import json

url = input('Enter URL: ')
if (len(url) < 1):
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

try:
    file = urllib.request.urlopen(url).read()
except:
    print('file not found')
    quit()

sum = 0
info = json.loads(file)
values = info['comments']
for value in values:
    sum = sum + int(value['count'])

print(sum)
