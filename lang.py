#!/usr/bin/python
import requests

url = "http://api06.dev.openstreetmap.org/"
#url = 'http://google.com'
payload = ('/api/capabilities')
r = requests.get(url, params=payload)

print r.status_code
print r.content
