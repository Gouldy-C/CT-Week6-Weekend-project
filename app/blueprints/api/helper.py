import requests
from app import app
from flask import jsonify
from flask_jwt_extended import get_jwt,create_access_token,get_jwt_identity
from datetime import datetime, timezone, timedelta

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


@app.after_request
def refresh_expiring_jwt(response):
    expiration = get_jwt()['exp']
    current  = datetime.now(timezone.utc)
    future_halfhour = datetime.timestamp(current + timedelta(minutes=30))
    if future_halfhour > expiration:
        access_token = create_access_token(identity= get_jwt_identity())
        data = response.get_json()
        data['access_token'] = access_token
        response.data = jsonify(data)
        return response