from flask import render_template, g
from flask_login import current_user, login_required

from app.blueprints.main.forms import SearchForm
from app import app
from . import bp as main


@app.before_request
def before_request():
    g.search_form = SearchForm()


@main.route('/')
def home():
    return render_template('main_home.jinja', search_form=g.search_form)


@main.post('/search-results')
@login_required
def search_results():
    pass