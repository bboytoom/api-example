from flask import request
from marshmallow import Schema, \
    fields, \
    validate, \
    pre_load, \
    post_load


class UserInformationSchema(Schema):
    class Meta:
        ordered = True

    user_uuid = fields.Str()

    address = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=50)
            ]
        )

    city = fields.Str(
        required=True,
        validate=[
            validate.Length(min=2, max=50)
            ]
        )

    state = fields.Str(
        required=True,
        validate=[
            validate.Length(min=2, max=50)
            ]
        )

    post_code = fields.Str(
        required=True,
        validate=[
            validate.Length(min=4, max=10),
            validate.Regexp(r'^[a-zA-Z0-9]*$')
            ]
        )

    country = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=30)
            ]
        )

    @pre_load
    def pre_load(self, data, **kwargs):
        if request.method in ['POST']:
            self.fields.get('user_uuid').required = False

        if request.method in ['PUT']:
            self.fields.get('user_uuid').required = False

        return data

    @post_load
    def post_load(self, data, **kwargs):
        data['address'] = data.get('address').lower().rstrip().lstrip()
        data['city'] = data.get('city').lower().rstrip().lstrip()
        data['state'] = data.get('state').lower().rstrip().lstrip()
        data['post_code'] = data.get('post_code').lower().rstrip().lstrip()
        data['country'] = data.get('country').lower().rstrip().lstrip()

        return data


schema_user_information = UserInformationSchema(exclude=('user_uuid',))
