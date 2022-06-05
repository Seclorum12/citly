from flask import Flask

import api
import blueprints
import db
import errorhandlers
import resourses

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# DB
db = db.DB(app)
db.create_all()

# API
api = api.API(app)
resourses.add_all(api)

blueprints.register_all(app)
errorhandlers.register_all(app)
