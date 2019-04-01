from marshmallow_jsonschema import JSONSchema

def json_schema(schema):
    # Fixes an hedge case: when "required "is empty "[]" then it must be removed, or it will throw error otherwise.
    return {k: v for k,v in next(iter(next(iter(JSONSchema().dump(schema).data.values())).values())).items()
            if k != 'required' or v}
