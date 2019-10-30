import json

with open('src/data/pokedex.json', 'r') as f:
    data_dict = json.load(f)

print(data_dict)