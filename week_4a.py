import urllib.request
from bs4 import BeautifulSoup

url = input("Enter - ")
if (len(url) < 1):
    url = "http://py4e-data.dr-chuck.net/comments_42.html"

file = urllib.request.urlopen(url).read()
info = BeautifulSoup(file, 'html.parser')

total = 0

tags = info('span')
for tag in tags:
    total = total + int(tag.contents[0])

print(total)
