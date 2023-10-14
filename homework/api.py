import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

payload = {}
headers = {}

r = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(r.text)

for item in data:
    id_value = item['id']
    title_value = item['title']
    complet_value = item['completed']

    print(id_value, title_value, complet_value)
