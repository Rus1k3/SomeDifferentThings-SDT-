import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

sortedJson = dict(sorted(sampleJson.items()))

with open('sorted.json', 'w') as json_file:
    json.dump(sortedJson, json_file, indent=4)