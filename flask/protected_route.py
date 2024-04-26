from flask import jsonify
from utils import get_token_from_header, verify_token


def protected_route(route_function):
    def cb(*args, **kwargs):
        token = get_token_from_header()
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        data, error_message = verify_token(token)
        if not data:
            return jsonify({"message": error_message}), 401

        return route_function(*args, **kwargs)

    return cb
