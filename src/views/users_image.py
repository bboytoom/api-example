from flask import jsonify
from flask.views import MethodView
from src.views.decorators.user_decorator import validate_method_parameters, \
    clean_request_user_image


class UsersImage(MethodView):

    @clean_request_user_image
    def post(self, data):

        return jsonify(
            result='post'
            )

    @validate_method_parameters
    def put(self, user_uuid):
        return jsonify(
            result='update'
            )

    @validate_method_parameters
    def delete(self, user_uuid):
        print(user_uuid)
        return jsonify(
            result='delete'
            )
