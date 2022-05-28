from dotenv import dotenv_values

env = dotenv_values(".env")

if env.get('FLASK_ENV') == 'development':
    from .dev import *
else:
    from .prod import *
