import functools
from flask import request, abort

from src.models.schemas.users_schema import UserSchema, UserImageSchema
from src.models.schemas.users_information_schema import UserInformationSchema


def clean_request_user(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type')
        schema_user = UserSchema()

        if content_type != 'application/json':
            return abort(400, 'Content-Type not supported!')

        errors = schema_user.validate(request.get_json())

        if errors:
            return abort(422, errors)

        return func(self, schema_user.load(request.get_json()), *args, **kwargs)

    return wrapper


def clean_request_user_image(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type')
        schema_user_image = UserImageSchema()

        if content_type is None or 'multipart/form-data' not in content_type:
            return abort(400, 'Content-Type not supported!')

        image = request.files
        errors = schema_user_image.validate(image)

        if errors:
            return abort(422, errors)

        return func(self, image.get('image', None), *args, **kwargs)

    return wrapper


def clean_request_user_information(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type')
        schema_user_information = UserInformationSchema()

        if content_type != 'application/json':
            return abort(400, 'Content-Type not supported!')

        errors = schema_user_information.validate(request.get_json())

        if errors:
            return abort(422, errors)

        return func(self, schema_user_information.load(request.get_json()), *args, **kwargs)

    return wrapper
