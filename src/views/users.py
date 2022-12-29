from flask import jsonify
from flask.views import MethodView

from src.models.User import User
from src.models.schemas.users_schema import schema_user, schemas_users
from src.views.decorators.user_decorator import clean_request_user_store


class Users(MethodView):
    def get(self, user_uuid):
        if user_uuid is None:
            return jsonify(
                data=schemas_users.dump(User.retrieve_all_user())
                )

        user = User.retrieve_user(user_uuid)

        if not user:
            return jsonify(
                result='uuid not exists'
                ), 404

        return jsonify(schema_user.dump(user))

    @clean_request_user_store
    def post(self, data):
        if User.exists_email(data.get('email')):
            return jsonify(
                result='email exists'
                ), 422

        user = User.new_user(data)

        return jsonify(
            result=user.create()
            ), 201

    @clean_request_user_store
    def put(self, data, user_uuid):
        user = User.retrieve_user(user_uuid)

        if not user:
            return jsonify(
                result='uuid not exists'
                ), 404

        if User.exists_email(data.get('email'), user_uuid):
            return jsonify(
                result='the email already exists'
                ), 422

        user.email = data.get('email')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.date_of_birth = data.get('date_of_birth')
        user.status = data.get('status')

        if User.update():
            return jsonify(
                result='update'
                )

        return jsonify(
            result='error'
            ), 400

    def delete(self, user_uuid):
        user = User.retrieve_user(user_uuid)

        if not user:
            return jsonify(
                result='uuid not exists'
                ), 404

        if User.delete(user_uuid):
            return '', 204

        return jsonify(
            result='error'
            ), 400
