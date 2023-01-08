import os
from flask import jsonify, abort, send_file
from flask.views import MethodView
from werkzeug.utils import secure_filename

from src.views.decorators.user_decorator import validate_method_parameters, \
    clean_request_user_image


class UsersImage(MethodView):
    def get(self, file_name):
        return send_file('../static/images/' + file_name)

    @validate_method_parameters
    @clean_request_user_image
    def post(self, data, user_uuid):
        filename = secure_filename(data.filename)

        data.seek(0)
        data.save(
            os.path.join(os.environ.get('URL_IMAGE'), filename)
            )

        user_uuid.image_name = filename

        if user_uuid.save():
            return jsonify(message='update image'), 301

        return abort(400)

    @validate_method_parameters
    def delete(self, user_uuid):
        user_uuid.image_name = None

        if user_uuid.save():
            return jsonify(message='update image'), 204

        return abort(400)
