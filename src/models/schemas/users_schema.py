from datetime import datetime

from flask import request
from marshmallow import Schema, \
    fields, \
    validate, \
    validates, \
    ValidationError, \
    pre_load, \
    post_load


class UserSchema(Schema):
    first_name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=2, max=30)
            ]
        )

    last_name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=2, max=30)
            ]
        )

    email = fields.Email(
        required=True,
        validate=[
            validate.Length(min=8, max=60)
            ]
        )

    password = fields.Str(
        required=True,
        load_only=True,
        validate=[
            validate.Length(min=8, max=15)
            ]
        )

    date_of_birth = fields.Date('%Y-%m-%d', required=True)

    @validates('date_of_birth')
    def is_not_in_future(self, value):
        min_birth = datetime.now()
        birth = value.strftime('%Y-%m-%d')

        if birth > min_birth.strftime('%Y-%m-%d'):
            raise ValidationError('The birthday should not be in the future.')

        if birth <= '1940-12-31':
            raise ValidationError('The birthday should be more that 1940-12-31.')

    @pre_load
    def pre_load(self, data, **kwargs):
        if request.method in ['PUT']:
            self.fields.get('password').required = False

        return data

    @post_load
    def post_load(self, data, **kwargs):
        data['last_name'] = data['last_name'].lower()
        data['first_name'] = data['first_name'].lower()
        data['email'] = data['email'].lower()

        return data
