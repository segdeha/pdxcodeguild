import urllib.request
import json
from datetime import datetime

handle = urllib.request.urlopen('http://api.randomuser.me/?results=5')
contents = handle.read()
text = contents.decode('utf-8')
data = json.loads(text)


def format_date(datestring):
    """Format dates like it’s 12/31/1999"""
    dt = datetime.fromtimestamp(datestring)
    return '{dt.month}/{dt.day}/{dt.year}'.format(dt=dt)

for person in data['results']:
    name = """{} {} {}""".format(
        person['name']['title'].title(),
        person['name']['first'].title(),
        person['name']['last'].title()
    )
    print("""    Name: {name}
    Email: {email}
    Username: {username}
    Registration date: {registration_date}
    Birth date: {birth_date}
    """.format(
        name=name,
        email=person['email'],
        username=person['login']['username'],
        registration_date=format_date(person['registered']),
        birth_date=format_date(person['dob'])
    ))
