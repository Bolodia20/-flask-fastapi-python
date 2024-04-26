from flask import request, jsonify, Blueprint
import uuid
from protected_route import protected_route

create_heath_status_router = Blueprint("create_heath_status_router", __name__)


@create_heath_status_router.post("/status")
@protected_route
def create_health_item():
    payload = request.json

    return jsonify({**payload, "id": uuid.uuid4()})
