import functools
from flask import request, jsonify
from src.models.schemas.users_schema import UserSchema


def clean_request_user_store(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type')
        schema_user = UserSchema()

        if (content_type != 'application/json'):
            return jsonify(
                errors={
                    'Content-Type': [
                        'Type not supported!'
                        ]
                    }
                ), 400

        errors = schema_user.validate(request.get_json())

        if errors:
            return jsonify(
                errors=errors
                ), 422

        return func(self, schema_user.load(request.get_json()), *args, **kwargs)

    return wrapper
