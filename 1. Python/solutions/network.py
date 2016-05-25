import urllib.request
import json

"""Fetch a resource over the network and display some of the data

Data format:

{
    "ip": "216.151.183.96",
    "about": "/about",
    "Pro!": "http://getjsonip.com"
}

"""

handle = urllib.request.urlopen('http://jsonip.com/')  # > Open a handle to the remote file
contents = handle.read()  # > Read the contents returned from the URL _in binary format_
text = contents.decode('utf-8')  # > Convert the binary response to text
data = json.loads(text)  # > Convert the JSON text into a data structure

print('Your IP address is: {ip}'.format(
    ip=data['ip']
))
