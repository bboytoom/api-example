import functools
from flask import request, jsonify, abort

from src.models.User import User
from src.models.schemas.users_schema import UserSchema, UserImageSchema


def clean_request_user_store(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type')
        schema_user = UserSchema()

        if content_type != 'application/json':
            return abort(400, 'Content-Type not supported!')

        errors = schema_user.validate(request.get_json())

        if errors:
            return jsonify(
                errors=errors
                ), 422

        return func(self, schema_user.load(request.get_json()), *args, **kwargs)

    return wrapper


def clean_request_user_image(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type')
        schema_user_image = UserImageSchema()

        if content_type is None or 'multipart/form-data' not in content_type:
            return abort(400, 'Content-Type not supported!')

        errors = schema_user_image.validate(request.files.to_dict(flat=False).get('image', []))

        print(errors)

        return func(self, None, *args, **kwargs)

    return wrapper


def validate_method_parameters(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        uuid = kwargs.get('user_uuid', None)

        if uuid is None:
            return func(self, uuid)

        user_uuid = User.query.filter_by(uuid=uuid).first_or_404()
        return func(self, user_uuid)

    wrapper.__name__ = func.__name__

    return wrapper
