from flask import Flask

# Import the Config Object
from config import Config

# import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# import the Migrate Object
from flask_migrate import Migrate 

# import for the Flask Login Module
from flask_login import LoginManager

app = Flask(__name__)
# Complete the Config cycle for our Flask App
# and Give access to our Database(When we have one)
# along with our Secret Key
app.config.from_object(Config)

# init our database (db)
db = SQLAlchemy(app)

# init the migrator
migrate = Migrate(app,db) 

# Login Config - Init for the LoginManager
login_manager = LoginManager(app)
# Specify what page to load for NON-authenticated users
login_manager.login_view = 'login'

from chicodes_blog_app import routes, models 