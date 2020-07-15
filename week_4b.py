import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
if (len(url) < 1):
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.htm'
count = int(input("Enter count: "))
position = int(input("Enter position: "))
name = ''

for i in range(0, count):
    file = urllib.request.urlopen(url).read()
    print('Retrieving: ', url)
    soup = BeautifulSoup(file, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    name = tags[position - 1].contents[0]
print(name)
