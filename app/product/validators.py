from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from sqlalchemy import text
from wtforms.validators import DataRequired, ValidationError
from sqlalchemy.orm import load_only
from app import db
from .models import Product, product_json_schema


def product_exists(filters):
    """Check that the products exists, raise error otherwise"""
    if not db.session.query(Product).filter(*filters).count():
        raise ValidationError('Product does not exist.')

def json_product_exists(form, field):
    product_exists([getattr(Product, k) == v for k,v in field.data.items()])

def id_product_exists(form, field):
    product_exists((Product.id == field.data,))

def product_not_exists(form, field):
    """Check that the products doesn't exist, raise error otherwise"""
    filters = [getattr(Product, k) == v for k,v in field.data.items()]
    if db.session.query(Product).filter(*filters).count():
        raise ValidationError('Product already exists.')


class ProductGetValidator(Inputs):
    rule = {
        'id': [DataRequired(), id_product_exists]
    }


class ProductPostValidator(Inputs):
    json = [JsonSchema(product_json_schema), product_not_exists]


class ProductPutValidator(Inputs):
    rule = {
        'id': [DataRequired(), id_product_exists]
    }
    json = [JsonSchema(product_json_schema)]
