from datetime import datetime
from flask import request, url_for
from marshmallow import Schema, \
    fields, \
    validate, \
    validates, \
    ValidationError, \
    pre_load, \
    post_load, \
    post_dump

from src.models.schemas.users_information_schema import schema_user_information


class UserImageSchema(Schema):
    image = fields.Raw(type='file', required=True)

    @validates('image')
    def valid_image(self, image):
        if not image:
            raise ValidationError('Empty file')

        if image.content_type not in {'image/jpeg', 'image/jpg', 'image/png'}:
            raise ValidationError('File type ' + image.content_type + ' no valid')

        if image.seek(0, 2)/1000 >= 2000:
            raise ValidationError('The image is very large the max is 2MB')

    @pre_load
    def pre_load(self, image, **kwargs):
        file = image.get('image', None)
        file.filename = file.filename.replace(' ', '_')

        return image


class UserSchema(Schema):
    class Meta:
        ordered = True

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
    image_name = fields.Str()
    information = fields.Nested(schema_user_information)

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
            self.fields.get('image_name').required = False

        if request.method in ['POST']:
            self.fields.get('uuid').required = False
            self.fields.get('status').required = False
            self.fields.get('image_name').required = False

        return data

    @post_load
    def post_load(self, data, **kwargs):
        data['last_name'] = data.get('last_name').lower().rstrip().lstrip()
        data['first_name'] = data.get('first_name').lower().rstrip().lstrip()
        data['email'] = data.get('email').lower()
        data['date_of_birth'] = data.get('date_of_birth').strftime('%Y-%m-%d')

        return data

    @post_dump(pass_many=True)
    def post_dump(self, data, **kwargs):
        if type(data) is list:
            for item in data:
                if item['image_name'] is not None:
                    item['image_name'] = url_for('static', filename='image/' + item['image_name'])
                else:
                    item.pop('image_name')

                if item['information'] is None:
                    item.pop('information')
        else:
            if data['image_name'] is not None:
                data['image_name'] = url_for('static', filename='image/' + data['image_name'])
            else:
                data.pop('image_name')

            if data['information'] is None:
                data.pop('information')

        return data


schema_user = UserSchema()
schemas_users = UserSchema(many=True)
