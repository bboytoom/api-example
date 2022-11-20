from flask import jsonify


def page_not_found(e):
    return jsonify(error=str(e)), 404


def internal_server_error(e):
    return jsonify(error=str(e)), 500


def ratelimit_handler(e):
    return jsonify(error=str(e)), 429