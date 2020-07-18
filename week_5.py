import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
if (len(url) < 1):
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

try:
    file = urllib.request.urlopen(url).read()
except:
    print('file not found')
    quit()

sum = 0
info = ET.fromstring(file)
tags = info.findall('comments/comment/count')
for tag in tags:
    sum = sum + int(tag.text)

print(sum)
