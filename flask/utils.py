from flask import request
from jose import jwt
from consts import ALGORITHM, SECRET_KEY
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_token_from_header():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    token_parts = auth_header.split(" ")
    if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
        return None
    return token_parts[1]


def verify_token(token):
    print("verify_token token", token)
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except jwt.ExpiredSignatureError:
        return None, "Token has expired"
    except (jwt.JWTError, Exception):
        return None, "Token is invalid!"


def verify_password(plain_password, user_password):
    return pwd_context.verify(plain_password, user_password)
