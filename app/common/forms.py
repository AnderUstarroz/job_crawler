from wtforms.csrf.core import CSRF
from flask import current_app
from wtforms import Form
from hashlib import md5
import os


class BasicCSRF(CSRF):

    def generate_csrf_token(self, csrf_token):
        token = md5(current_app.config['SECRET_KEY']).hexdigest()
        return token

class CSRFForm(Form):

    class Meta:
        csrf = True  # Enable CSRF
        csrf_class = BasicCSRF  # Set the CSRF implementation
        csrf_secret = os.urandom(16)  # Secret key.
        # Any other CSRF settings here.
