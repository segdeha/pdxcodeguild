"""Fun with Network I/O Solution"""

import urllib.request
import json
from datetime import datetime

handle = urllib.request.urlopen('http://api.randomuser.me/?results=5')
contents = handle.read()
text = contents.decode('utf-8')
data = json.loads(text)


def format_date(timestamp):
    """Format dates like it’s 12/31/1999"""
    dt = datetime.fromtimestamp(timestamp)
    return '{dt.month}/{dt.day}/{dt.year}'.format(dt=dt)

for person in data['results']:
    print("""Name: {title} {first} {last}
Email: {email}
Username: {username}
Registration date: {registration_date}
Birth date: {birth_date}
""".format(
        title=person['name']['title'].title(),
        first=person['name']['first'].title(),
        last=person['name']['last'].title(),
        email=person['email'],
        username=person['login']['username'],
        registration_date=format_date(person['registered']),
        birth_date=format_date(person['dob'])
    ))
