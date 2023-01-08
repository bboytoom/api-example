from flask import jsonify, request


def bad_request_handler(e):
    return jsonify(
        error=e.name,
        exception=str(e),
        path=request.path,
        method=request.method
        ), 400


def page_not_found(e):
    return jsonify(
        error=e.name,
        exception=str(e),
        path=request.path,
        method=request.method
        ), 404


def method_not_allow_handler(e):
    return jsonify(
        error=e.name,
        exception=str(e),
        path=request.path,
        method=request.method
        ), 405


def unprocessable_entity(e):
    return jsonify(
        error=e.name,
        exception=e.description,
        path=request.path,
        method=request.method
        ), 422


def rate_limit_handler(e):
    return jsonify(
        error=e.name,
        exception=str(e),
        path=request.path,
        method=request.method
        ), 429


def internal_server_error(e):
    return jsonify(
        error=e.name,
        exception=str(e),
        path=request.path,
        method=request.method
        ), 500
