from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from ConfigMod import Config




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

login_manager.login_view = 'auth.signin'
login_manager.login_message = 'Login you filthy animal'
login_manager.login_message_category = 'warning'


from app.blueprints.main import bp as main
app.register_blueprint(main)
from app.blueprints.auth import bp as auth
app.register_blueprint(auth)
from app.blueprints.account import bp as account
app.register_blueprint(account)
from app.blueprints.api import bp as api
app.register_blueprint(api)

from app import models