from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_caching import Cache
from flask_login import LoginManager
from .common.exceptions import page_not_found


db = SQLAlchemy()
cache = Cache()
login_manager = LoginManager()
marshmallow = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config/settings.py')
    app.secret_key = app.config['SECRET_KEY']
    login_manager.init_app(app)
    cache.init_app(app, config=app.config["CACHE"])
    marshmallow.init_app(app)
    db.init_app(app)
    app.register_error_handler(404, page_not_found)

    # IMPORTANT! These imports must be placed after db, cache creation to avoid circular import issues
    from .product.models import Product
    from .product.views import ProductView

    ProductView.register(app)
    db.create_all(app=app)
    return app


#@app.context_processor
#def template_vars():
#    return dict(common={'a':1,'b':current_user})


def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all(app=app)

