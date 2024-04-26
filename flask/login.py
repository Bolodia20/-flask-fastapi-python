from flask import request, jsonify, Blueprint
from jose import jwt
import datetime
from mock_up_data import fake_users
from consts import ALGORITHM, SECRET_KEY
from utils import verify_password


login_router = Blueprint("login_router", __name__)


@login_router.post("/login")
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username or password missing"}), 400

    user = fake_users.get(username)
    is_valid_password = verify_password(password, user.get("password"))

    if user and is_valid_password:
        token = jwt.encode(
            {
                "user": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            SECRET_KEY,
            algorithm=ALGORITHM,
        )
        return jsonify({"access_token": token, "token_type": "bearer"})

    return jsonify({"message": "Invalid username or password"}), 401
