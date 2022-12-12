from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    email = fields.Str(
        required=True,
        validate=[
            validate.Email(error="Not a valid email address"),
            validate.Length(max=70)
            ]
        )

    # password = fields.Str(required=True)
    # first_name = fields.Str(required=True)
    # last_name = fields.Str(required=True)
    # date_of_birth  = fields.Date(required=True)
