import json
import csv
import requests


response = requests.get('http://rtl2.ods-live.co.uk/api/vehiclePositionHistory?key=wyFhgvh701&date=2017-03-24&vehicle=&from=00:00:00&to=23:59:59').content
response = json.loads(response)

data = []
for resp in response:
    data.append({'date': resp['observed'], 'lat': resp['latitude'], 'lon': resp['longitude']})

print len(data)

f = csv.writer(open("test.csv", "wb+"))

f.writerow(["date", "lat", "lon"])

for d in data:
    f.writerow([d['date'], d['lat'], d['lon']])
