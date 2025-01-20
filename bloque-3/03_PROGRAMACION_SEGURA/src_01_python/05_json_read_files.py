import json

with open('json_data.json') as json_file:
    data = json.load(json_file)
    
print("type(data):", type(data))
print("data:", json.dumps(data, indent=2))

