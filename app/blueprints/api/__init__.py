from flask import Blueprint

bp = Blueprint('api',__name__,template_folder='templates',url_prefix='/api')

from . import auth_routes, account_routes