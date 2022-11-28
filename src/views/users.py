from flask import request


def retrieve():
    """
    Retrieve all users
    """

    return {'result': 'retrieve'}


def store():
    """
    Create user
    """

    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        json = request.get_json()

        return {
            'result': 'store',
            'data': json
            }, 201
    else:
        return {
            'result': 'Content-Type not supported!'
            }, 400
