"""DOCSTRING."""

import json
import csv
import requests


data = []
for hour in range(0, 24, 1):
    print 'HOUR ', hour
    for minute in range(0, 6010):

        magic = 'http://rtl2.ods-live.co.uk/api/vehiclePositionHistory?key=wyFhgvh701&date=2017-03-24&vehicle=&from={:02d}:{:02d}:00&to={:02d}:{:02d}:59'.format(hour, minute, hour, minute+9)

        response = requests.get(magic).content
        response = json.loads(response)

        for resp in response:
            data.append({'timestamp': resp['observed'], 'latitude': resp['latitude'], 'longitude': resp['longitude'], 'vehicle': resp['vehicle']})

f = csv.writer(open("test.csv", "wb+"))

f.writerow(["timestamp", "vehicle", "latitude", "longitude"])

for d in data:
    f.writerow([d['timestamp'], d['vehicle'], d['latitude'], d['longitude']])
