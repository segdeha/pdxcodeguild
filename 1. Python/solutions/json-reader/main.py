import json

"""

Format of data.json:

{
    "locality": "Portland",
    "location": {
        "type": "Point",
        "coordinates": [-122.676207, 45.523452]
    }
}

"""

with open('data.json', 'r') as f:
    contents = f.read()
    data = json.loads(contents)

print('The Latitude/Longitude of {locality} is {lat}/{lng}.'.format(
    locality=data['locality'],
    lat=data['location']['coordinates'][1],
    lng=data['location']['coordinates'][0]
))
