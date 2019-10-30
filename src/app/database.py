import json

def init_app():
    with open('src/data/pokedex.json', 'r') as f:
        data_dict = json.load(f)

    for index, data in enumerate(data_dict, 1):
        data['name'] = data['name']['english']
        data['image_url'] = 'https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/{:03d}.png'.format(index)
        data.pop('type')
        data.pop('base')

    return data_dict