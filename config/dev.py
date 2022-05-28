from .base import *  # noqa

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR.joinpath('dev.db'))
