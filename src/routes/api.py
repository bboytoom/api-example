from flask import Blueprint
from src.views.users import Users

api = Blueprint('api', __name__,  url_prefix='/api/v1')

user_api = Users.as_view('users')

api.add_url_rule('/users', view_func=user_api, defaults={'user_uuid': None}, methods=['GET'])
api.add_url_rule('/users', view_func=user_api, methods=['POST'])
api.add_url_rule('/users/<uuid:user_uuid>', view_func=user_api, methods=['GET', 'PUT', 'DELETE'])
