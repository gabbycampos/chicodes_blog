# import the os module
import os 

# creation of base directory for application. Will find the document on whatever machine your on
basedir = os.path.abspath(os.path.dirname(__file__))
# for ex:
# Mac & Linux = Desktop/ChiCodes/week5/chicodes_blog

# Config Class
# Configure the database (when we have one) AND configure the secret
# key for the encryption of our submitted forms 
class Config():
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this....'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATION = False