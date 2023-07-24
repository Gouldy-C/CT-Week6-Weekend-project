from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from random import shuffle

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    pokedex = db.relationship('Pokedex', backref='trainer', lazy=True)
    teams = db.relationship('Team', backref='trainer', lazy=True)
    
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def from_dict(self, user_dict):
        for k, v in user_dict.items():
            if k == 'email':
                setattr(self, k, v.lower())
            else:
                setattr(self, k, v)
    
    
    def to_dict(self):
        return {
            'username' : self.username,
            'email' : self.email,
            'pokedex' : [{'pokemon_name': pokemon.pokemon_id,
                        'pokemon_id': pokemon.name} for pokemon in self.pokedex],
            'teams' : [[team.name,[poke for poke in team.pokemon.name]] for team in self.teams]
        }



class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    base_exp = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.String(), nullable=False)
    types = db.Column(db.String(), nullable=False)
    moves = db.Column(db.String(), nullable=False)
    
    
    def pick_rand_moves(self, lst):
        res = []
        for x in range(4):
            shuffle(lst)
            res.append(lst.pop())
        self.moves = ', '.join(res)
        return True
    
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    team_name = db.Column(db.String(255), nullable=False)
    num_pokemon = db.Column(db.Integer)
    pokemon = db.relationship('TeamPokemon', backref='team', lazy=True)
    
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class TeamPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"), nullable=False)
    pokemon_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(), nullable=False)
    
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()