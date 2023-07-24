from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from ConfigMod import Config




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)



from app.blueprints.main import bp as main
app.register_blueprint(main)
from app.blueprints.auth import bp as auth
app.register_blueprint(auth)
from app.blueprints.account import bp as account
app.register_blueprint(account)

from app import models