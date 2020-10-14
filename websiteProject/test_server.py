import requests
import json

SITE_URL = 'http://localhost:51068'
EVENT_URL = SITE_URL + '/events/'
COUNTRIES_URL = SITE_URL + '/countries/'
YEARS_URL = SITE_URL + '/years/'

print(json.loads(requests.get(EVENT_URL + '201712310032').content.decode()))

print(len(json.loads(requests.get(COUNTRIES_URL + 'United States').content.decode())['data']))

print(json.loads(requests.get(YEARS_URL + '1970').content.decode()))




