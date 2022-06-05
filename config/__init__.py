from os import environ

flask_env = environ.get('FLASK_ENV')

if flask_env == 'development':
    from .dev import *
elif flask_env == 'testing':
    from .testing import *
else:
    from .prod import *
