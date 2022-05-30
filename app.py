from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import blueprints
import errorhandlers
import resourses
import api

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# DB
db = SQLAlchemy(app)

# API
api = api.API(app)
resourses.add_all(api)

blueprints.register_all(app)
errorhandlers.register_all(app)

db.create_all()
