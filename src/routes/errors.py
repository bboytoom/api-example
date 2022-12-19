import logging
from flask import jsonify

logger = logging.getLogger(__name__)


def bad_request_handler(e):
    logger.error(e)

    return jsonify(error=str(e)), 400


def page_not_found(e):
    logger.error(e)

    return jsonify(error=str(e)), 404


def method_not_allow_handler(e):
    logger.error(e)

    return jsonify(error=str(e)), 405


def rate_limit_handler(e):
    logger.error(e)

    return jsonify(error=str(e)), 429


def internal_server_error(e):
    logger.error(e)

    return jsonify(error=str(e)), 500
