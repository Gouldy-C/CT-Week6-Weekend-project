from flask import render_template, flash, redirect, url_for, g, request
from flask_login import login_required, current_user

from . import bp as account
from app import app
from app.blueprints.account.forms import PokeDataForm
from app.models import User, Pokedex, Team, TeamPokemon
from app.blueprints.api.helper import get_dict_info_pokemon, get_all_pokemon_dict


@app.before_request
def before_request():
    g.poke_data_form = PokeDataForm()


@account.route('/account/<username>')
@login_required
def home(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('account.jinja', user=user, search_form=g.search_form, pokedex=user.pokedex, poke_data_form=g.poke_data_form)
    else:
        flash(f'User: {username} not found', category='warning')
        return redirect(url_for('main.home', search_form=g.search_form, poke_data_form=g.poke_data_form))


@account.route('/search/<search>', methods=['GET', 'POST'])
@login_required
def general_search(search):
    search = search.strip()
    count = 0
    user = User.query.filter_by(username=search).first()
    if not user:
        user = None
    else:
        count = Pokedex.query.filter_by(user_id=user.id).count()
    search = search.lower()
    pokemon = get_all_pokemon_dict()
    if search in pokemon.keys():
        poke_dict = get_dict_info_pokemon(search)
    else: 
        poke_dict = None
    return render_template('general_search.jinja',pokemon=poke_dict, user=user, search=search, search_form=g.search_form, count=count, poke_data_form=g.poke_data_form)

@account.post('/search-form')
@login_required
def form_search():
    search = g.search_form.search.data
    return redirect(url_for('account.general_search', search=search))


@account.post('/add-to-pokedex')
@login_required
def add_to_pokedex():
    if g.poke_data_form.validate_on_submit():
        pokemon = g.poke_data_form.poke_name.data
    try:
        poke_info = get_dict_info_pokemon(pokemon)
        pe = Pokedex()
        pe.user_id = current_user.id
        pe.name = poke_info['name']
        pe.pokemon_id = poke_info['pokemon_id']
        pe.height = poke_info['height']
        pe.weight = poke_info['weight']
        pe.base_exp = poke_info['base_exp']
        pe.sprite = poke_info['sprite']
        pe.types = ', '.join(poke_info['types'])
        pe.pick_rand_moves(list(poke_info['moves'].keys()))
        pe.commit()
        flash(f'{pokemon.title()} has been added to your PokeDex.', category='success')
        return redirect(url_for('account.home', username=current_user.username,search_form=g.search_form, poke_data_form=g.poke_data_form))
    except:
        flash(f'{pokemon.title()} is already in your PokeDex or does not exist.', category='warning')
        return redirect(url_for('account.home', username=current_user.username, search_form=g.search_form,  poke_data_form=g.poke_data_form))
    
    

    
    
    