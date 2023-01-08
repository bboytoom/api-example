from flask import Blueprint
from src.views.users_image import UsersImage

web = Blueprint('web', __name__)

user_image = UsersImage.as_view('user_image')
web.add_url_rule('/static/image/<file_name>', view_func=user_image, methods=['GET'])
