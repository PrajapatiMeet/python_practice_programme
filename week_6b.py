import urllib.request, urllib.parse
import json

api_key = 42
original_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    location = input("Enter Location: ")
    if (len(location) < 1):
        break

    parms = dict()
    parms['address'] = location
    parms['key'] = api_key
    url =  original_url + urllib.parse.urlencode(parms)

    print('Retrieve:', url)
    data = urllib.request.urlopen(url).read().decode()
    print('Retrived', len(data), 'Characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('can not find')
        print(data)
        continue

    place_id = js['results'][1]['place_id']
    print('place_id',place_id)
