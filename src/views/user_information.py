from flask import jsonify, abort
from flask.views import MethodView

from src.models.Information import Information
from src.views.decorators.user_decorator import clean_request_user_information
from src.views.decorators.parameters_decorator import parameters_user, \
    parameters_user_information


class UsersInformation(MethodView):

    @parameters_user
    @clean_request_user_information
    def post(self, data, user_uuid):
        if Information.exists_user_uuid(user_uuid.uuid):
            return abort(422, {'user_uuid': ['The information has already been added']})

        data.update({'user_uuid': user_uuid.uuid})
        information = Information.new_user_information(data)

        if information.save():
            return jsonify(
                message='added'
                ), 201

        return abort(400)

    @parameters_user_information
    @clean_request_user_information
    def put(self, data, user_uuid):
        user_uuid.address = data.get('address')
        user_uuid.state = data.get('state')
        user_uuid.city = data.get('city')
        user_uuid.country = data.get('country')
        user_uuid.post_code = data.get('post_code')

        if user_uuid.save():
            return jsonify(message='updated')

        return abort(400)

    @parameters_user_information
    def delete(self, user_uuid):
        if user_uuid.delete():
            return '', 204

        return abort(400)
