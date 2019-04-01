from flask import url_for
from .factories import ProductFactory
from .models import Product


def test_app(session, client):
    product = ProductFactory.create()
    assert client.get(url_for('ProductView:get', id=0)).status_code == 200
    assert session.query(Product).count() > 0
