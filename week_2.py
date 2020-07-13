import urllib.request, urllib.parse, urllib.error
import re

fname = input("Enter name of file : ")
file = urllib.request.urlopen(fname)
sum = 0
for line in file:
    line = line.decode().strip()
    values = re.findall("[0-9]+", line)
    for num in values:
        sum = sum + int(num)
print(sum)
