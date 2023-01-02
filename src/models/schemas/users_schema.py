from datetime import datetime

from flask import request
from marshmallow import Schema, \
    fields, \
    validate, \
    validates, \
    ValidationError, \
    pre_load, \
    post_load


class UserImageSchema(Schema):
    image = fields.Raw(metadata={'type': 'image'})


class UserSchema(Schema):
    uuid = fields.Str()

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
    status = fields.Bool(required=True)

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
            self.fields.get('uuid').required = False
            self.fields.get('password').required = False

        if request.method in ['POST']:
            self.fields.get('uuid').required = False
            self.fields.get('status').required = False

        return data

    @post_load
    def post_load(self, data, **kwargs):
        data['last_name'] = data.get('last_name').lower().rstrip().lstrip()
        data['first_name'] = data.get('first_name').lower().rstrip().lstrip()
        data['email'] = data.get('email').lower()
        data['date_of_birth'] = data.get('date_of_birth').strftime('%Y-%m-%d')

        return data


schema_user = UserSchema()
schemas_users = UserSchema(many=True)
