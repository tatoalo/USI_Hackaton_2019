import requests
import numpy as np
import json
import random
COUNT = 100

bikes = requests.get('http://localhost:5000/stations/bike').json()
tpl = requests.get('http://localhost:5000/stations/tpl').json()

coords = {}
rand_points  = {}
coords['bike'] = [ (b['coords']['lat'], b['coords']['lon']) for b in bikes]
coords['bus'] = [ (t['coords']['lat'], t['coords']['lon']) for t in tpl]

rand_points['bike'] = []
rand_points['bus'] = []
for l in ['bike', 'bus']:

    for i in range(COUNT):
        print(coords[l])
        start = random.choice(coords[l])
        coords[l].remove(start)
        end = random.choice(coords[l])
        coords[l].append(start)
        rand_points[l].append((start,end))
        requests.put('http://localhost:5000/users/1', data=json.dumps({
            'type':l,
            'lat_start':start[0],
            'lon_start':start[1],
            'lat_end':end[0],
            'lon_end':end[1]}))
#print(rand_points)
