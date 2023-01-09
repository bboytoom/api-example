from flask import jsonify, abort
from flask.views import MethodView

from src.models.User import User
from src.models.schemas.users_schema import schema_user, schemas_users
from src.views.decorators.user_decorator import clean_request_user
from src.views.decorators.parameters_decorator import parameters_user


class Users(MethodView):

    @parameters_user
    def get(self, user_uuid):
        if user_uuid is None:
            return jsonify(
                data=schemas_users.dump(User.retrieve_all_user())
                )

        return jsonify(schema_user.dump(user_uuid))

    @clean_request_user
    def post(self, data):
        if User.exists_email(data.get('email')):
            return abort(422, 'The email already exists')

        user = User.new_user(data)

        if user.save():
            return jsonify(
                message='added',
                user_uuid=user.uuid
                ), 201

        return abort(400)

    @parameters_user
    @clean_request_user
    def put(self, data, user_uuid):
        if User.exists_email(data.get('email'), user_uuid.uuid):
            return abort(422, 'The email already exists')

        user_uuid.email = data.get('email')
        user_uuid.first_name = data.get('first_name')
        user_uuid.last_name = data.get('last_name')
        user_uuid.date_of_birth = data.get('date_of_birth')
        user_uuid.status = data.get('status')

        if user_uuid.save():
            return jsonify(message='updated')

        return abort(400)

    @parameters_user
    def delete(self, user_uuid):
        if user_uuid.delete():
            return '', 204

        return abort(400)
