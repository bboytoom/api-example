from flask import jsonify
from flask.views import MethodView
from src.views.decorators.user_decorator import clean_request_user_store


class Users(MethodView):
    def get(self, user_uuid):
        if user_uuid is None:
            return jsonify(
                result='retrieve'
                )

        return jsonify(
            result='get',
            uuid=user_uuid
            )

    @clean_request_user_store
    def post(self, data):
        return jsonify(
            result='store'
            ), 201

    @clean_request_user_store
    def put(self, data, user_uuid):
        return jsonify(
            result='update'
            )

    def delete(self, user_uuid):
        return '', 204
