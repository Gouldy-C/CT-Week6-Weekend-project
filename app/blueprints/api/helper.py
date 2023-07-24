import requests

all_pokemon_dict = {}
all_pokemon_info_dict = {}

def get_all_pokemon_dict():
    global all_pokemon_dict
    if not all_pokemon_dict:
        api_url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
        response = requests.get(api_url).json()
        for pokemon in response['results']:
            all_pokemon_dict[pokemon['name']] = pokemon['url']
    return all_pokemon_dict


def get_dict_info_pokemon(name):
    global all_pokemon_info_dict
    if name not in all_pokemon_info_dict:
        api_url = 'https://pokeapi.co/api/v2/pokemon/' + name
        response = requests.get(api_url).json()
        all_pokemon_info_dict[response['name']] = {
            'name': response['name'],
            'pokemon_id': response['id'],
            'height': response['height'],
            'weight': response['weight'],
            'base_exp': response['base_experience'],
            'sprite': response['sprites']['front_default'],
            'moves': {move['move']['name']: move['move']['url'] for move in response['moves']},
            'types': [type['type']['name'] for type in response['types']]
        }
    return all_pokemon_info_dict[name]