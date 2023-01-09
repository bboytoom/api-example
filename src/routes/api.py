from flask import Blueprint
from src.views.users import Users
from src.views.users_image import UsersImage
from src.views.user_information import UsersInformation

api = Blueprint('api', __name__,  url_prefix='/api/v1')

# URL's to insert, update, delete and get users
user_api = Users.as_view('users')

api.add_url_rule('/users', view_func=user_api, defaults={'user_uuid': None}, methods=['GET'])
api.add_url_rule('/users', view_func=user_api, methods=['POST'])
api.add_url_rule('/users/<uuid:user_uuid>', view_func=user_api, methods=['GET', 'PUT', 'DELETE'])

# URL's to insert, update and delete information of the user
user_information = UsersInformation.as_view('user_information')

api.add_url_rule(
    '/users/<uuid:user_uuid>/information',
    view_func=user_information,
    methods=['POST', 'PUT', 'DELETE']
    )

# URL's to insert and delete image of the users
user_image = UsersImage.as_view('user_image')

api.add_url_rule(
    '/users/<uuid:user_uuid>/user-image',
    view_func=user_image,
    methods=['POST', 'DELETE']
    )
