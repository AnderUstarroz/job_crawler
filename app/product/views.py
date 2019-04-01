from flask import current_app, request, jsonify
from .validators import ProductGetValidator, ProductPostValidator, ProductPutValidator
from .models import Product, product_schema
from app.common.helpers import pagination
from app import cache, db
from flask_classful import FlaskView
import json


class ProductView(FlaskView):

    def index(self):
        start = request.args.get('start', 1)
        limit = request.args.get('limit', current_app.config['PAGE_LIMIT'])
        pages = pagination(Product, request.base_url, start, limit)
        return jsonify(success=True, data={
            'previous': pages['previous'],
            'next': pages['next'],
            'results': [product_schema.dump(p).data for p in pages['results']]
        })

    def get(self, id):
        inputs = ProductGetValidator(request)
        if not inputs.validate():
            return jsonify(success=False, errors=inputs.errors)

        return jsonify(success=True, data=product_schema.dump(Product.query.get(id)).data)

    def post(self):
        inputs = ProductPostValidator(request)
        if not inputs.validate():
            return jsonify(success=False, errors=inputs.errors)

        product = Product(**json.loads(request.data))
        db.session.add(product)
        db.session.commit()
        return jsonify(success=True, data=product_schema.dump(product).data)

    def put(self, id):
        inputs = ProductPutValidator(request)
        if not inputs.validate():
            return jsonify(success=False, errors=inputs.errors)

        db.session.query(Product).filter_by(id=id).update(json.loads(request.data))
        db.session.commit()
        return jsonify(success=True, data=product_schema.dump(db.session.query(Product).get(id)).data)
