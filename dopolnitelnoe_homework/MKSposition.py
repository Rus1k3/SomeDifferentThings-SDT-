import requests
import json
import datetime

url = "https://api.wheretheiss.at/v1/satellites/25544"
response = requests.get(url)

jsos = json.dumps(response.json())

al = response.json()['altitude']

alt = int(al)

now = datetime.datetime.now()
forti = now.strftime('%H:%M')

print('Московское время', forti,'мкс на высоте', alt, 'километров над землей, если точнее то', al, 'километров')


