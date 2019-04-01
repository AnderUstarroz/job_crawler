from sqlalchemy import Column, Integer, String
from app import marshmallow
from app.common.validators import json_schema
from app import db


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name


class ProductSchema(marshmallow.ModelSchema):
    class Meta:
        model = Product


product_schema = ProductSchema(strict=True)
product_json_schema = json_schema(product_schema)

