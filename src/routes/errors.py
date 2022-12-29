from flask import jsonify, request


def bad_request_handler(e):
    return jsonify(
        error='Bad Request',
        exception=str(e),
        path=request.path,
        method=request.method
        ), 400


def page_not_found(e):
    return jsonify(
        error='Page Not Found',
        exception=str(e),
        path=request.path,
        method=request.method
        ), 404


def method_not_allow_handler(e):
    return jsonify(
        error='Method Not Allow',
        exception=str(e),
        path=request.path,
        method=request.method
        ), 405


def unprocessable_entity(e):
    return jsonify(
        error='Unprocessable Entity',
        exception=str(e),
        path=request.path,
        method=request.method
        ), 422


def rate_limit_handler(e):
    return jsonify(
        error='Rate Limit',
        exception=str(e),
        path=request.path,
        method=request.method
        ), 429


def internal_server_error(e):
    return jsonify(
        error='Server Internal Error',
        exception=str(e),
        path=request.path,
        method=request.method
        ), 500
