import factory
from .models import Product
from app import db


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = None   # the SQLAlchemy session object will be added on conftest.py

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: u'Product %d' % n)
