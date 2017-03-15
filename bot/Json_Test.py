import urllib.request
import json

# geourl = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
# response = urllib.request.urlopen(geourl)
# content = response.read()
# data = json.loads(content.decode("utf8"))
# print(data)
# print(data['type'])

book = {}
book['tom']={
    'name':'tom',
    'addres':'1 ave'
}
book['bob']={
    'name':'bob',
    'addres':'6 ave'
}
print(book)
print('-----------------')
data = (json.dumps(book))
print(type(book))

with open('jsontest.txt', 'w') as f:
    f.write(data)

with open('jsontest.txt', 'r') as f:
    s = f.read()
print('read ',s)
print(type(s))
dic = json.loads(s)
print(type(dic))
print(book['tom'])
for person in book:
    print(book[person])