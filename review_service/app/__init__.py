from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


path = os.path.abspath(os.path.dirname(__file__)) + "/../instance/development.cfg"
app = Flask(__name__)
app.config.from_pyfile(path)
db = SQLAlchemy(app)


ml_model_path = os.path.abspath(os.path.dirname(__file__)) + '/ml/models/'

def create_app(config_filename=None):
  application = Flask( 'reviews', instance_relative_config=True)
  application.config.from_pyfile(config_filename)
  initialize_extensions(application)
  register_blueprints(application)
  
  return application

def initialize_extensions(application):
  from app.models.reviews import Review

  db = SQLAlchemy(application)


def register_blueprints(application):
  from app.controllers import reviews_blueprints
  application.register_blueprint(reviews_blueprints)




