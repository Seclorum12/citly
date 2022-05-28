from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import blueprints
import errorhandlers

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# DB
db = SQLAlchemy(app)

blueprints.register_all(app)
errorhandlers.register_all(app)

db.create_all()
