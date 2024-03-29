from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Importing flask-login
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login Redirect Config
login = LoginManager(app)
login.login_view = 'login' # This specifies what page to load for non-authorized users


from finalproject import routes, models
