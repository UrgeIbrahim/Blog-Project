from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# GENERAL FLASK CONFIGURATION:
# https://flask.palletsprojects.com/en/2.0.x/config/
app.config['SECRET_KEY'] = 'ec9d598b21679a28f1daf57a6884923e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # allows you to put a login_required decorator
login_manager.login_message_category = 'info'

from flaskblog import routes
