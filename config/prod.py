from .base import *  # noqa

DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.joinpath('prod.db'))
