from flask import Blueprint
from src.views.users import retrieve

api = Blueprint('api', __name__,  url_prefix='/api/v1')

api.route('/users', methods=['GET'])(retrieve)
