from .base import *  # noqa

TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.joinpath('testing.db'))
