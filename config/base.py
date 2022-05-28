from pathlib import Path

from . import env

BASE_DIR = Path(__file__).parent.parent.absolute()
print(f'BASE_DIR is {BASE_DIR}')

DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = env.get('CSRF_SESSION_KEY')

SECRET_KEY = env.get('SECRET_KEY')
