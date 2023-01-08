from flask import Blueprint
from src.views.users import Users
from src.views.users_image import UsersImage

api = Blueprint('api', __name__,  url_prefix='/api/v1')

user_api = Users.as_view('users')

# URL's to insert basic user information
api.add_url_rule('/users', view_func=user_api, defaults={'user_uuid': None}, methods=['GET'])
api.add_url_rule('/users', view_func=user_api, methods=['POST'])
api.add_url_rule('/users/<uuid:user_uuid>', view_func=user_api, methods=['GET', 'PUT', 'DELETE'])

user_image = UsersImage.as_view('user_image')

# URL's to insert image of the users
api.add_url_rule(
    '/users/<uuid:user_uuid>/user-image',
    view_func=user_image,
    methods=['POST', 'DELETE']
    )
