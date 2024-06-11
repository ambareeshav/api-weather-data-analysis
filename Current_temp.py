import requests
import json
from requests.auth import HTTPBasicAuth
import time

response_API = requests.get('http://api.weatherapi.com/v1/current.json?key=fb0bc518316645c4b10114248240306&q=13.036791,80.267632&aqi=no')
#print(response_API.status_code)

data = json.loads(response_API.text)

active = data['current']['temp_c']
print(active)

'''with open('api_data.txt', 'w') as convert:
    convert.write(json.dumps(data))'''
"""print(data)
parse_json= json.loads(data)
"""