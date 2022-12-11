import logging
from flask import jsonify

logger = logging.getLogger(__name__)


def page_not_found(e):
    return jsonify(error=str(e)), 404


def internal_server_error(e):
    logger.error(e)

    return jsonify(error=str(e)), 500


def ratelimit_handler(e):
    return jsonify(error=str(e)), 429
