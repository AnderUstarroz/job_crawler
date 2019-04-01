import os

DEBUG = True  # Turns on debugging features in Flask
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/development.db'.format(BASE_DIR)
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deprecated: Will add significant overhead
SECRET_KEY = b'02^D3.E9<?X=DLA%7[*TTV'  # Secret key for signing cookies/CSRF
MAIL_SERVER: 'localhost'
MAIL_PORT: 25
MAIL_USE_TLS: False
MAIL_USE_SSL: False
MAIL_DEBUG: DEBUG
MAIL_USERNAME: None
MAIL_PASSWORD: None
MAIL_DEFAULT_SENDER: None
CACHE = {
    'CACHE_TYPE': "simple",
}
CACHE = {
    'CACHE_TYPE': "simple",
}
