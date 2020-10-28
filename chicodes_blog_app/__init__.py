from flask import Flask

# Import the Config Object
from config import Config

# import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# import the Migrate Object
from flask_migrate import Migrate 

app = Flask(__name__)
# Complete the Config cycle for our Flask App
# and Give access to our Database(When we have one)
# along with our Secret Key
app.config.from_object(Config)

# init our database (db)
db = SQLAlchemy(app)

# init the migrator
migrate = Migrate(app,db) 

from chicodes_blog_app import routes, models 