import os
DEBUG = True  # Turns on debugging features in Flask
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/test.db'.format(BASE_DIR)
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deprecated: Will add significant overhead
SECRET_KEY = b'02^D3.E9<?X=DLA%7[*TTV'  # Secret key for signing cookies/CSRF
CACHE = {
    'CACHE_TYPE': 'null'
}