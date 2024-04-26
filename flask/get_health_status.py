from mock_up_data import mock_up_health_data

from flask import Blueprint, jsonify

get_health_data_router = Blueprint("get_health_data_router", __name__)


@get_health_data_router.get("/health")
def get_health_data():
    return jsonify({"data": mock_up_health_data})
