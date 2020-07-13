import urllib.request, urllib.parse, urllib.error
import re

fname = input("Enter name of file : ")
if (len(fname) < 1):
    fname = 'http://py4e-data.dr-chuck.net/regex_sum_576144.txt'

try:
    file = urllib.request.urlopen(fname)
except:
    print('file not found')
    quit()

sum = 0
for line in file:
    line = line.decode().strip()
    values = re.findall("[0-9]+", line)
    for num in values:
        sum = sum + int(num)
print(sum)
