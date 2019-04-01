import os


DEBUG = False
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
APP_NAME = 'app'
PAGE_LIMIT = 2

if os.environ.get('APP_ENV') == 'production':
    from config.production import *

elif os.environ.get('APP_ENV') == 'testing':
        from config.testing import *
else:
    from config.development import *
