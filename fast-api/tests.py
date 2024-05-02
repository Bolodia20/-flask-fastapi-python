from consts import ALGORITHM, SECRET_KEY
from utils import (
    create_access_token,
    verify_password,
    pwd_context,
    get_user,
    authenticate_user,
)
from jose import jwt, JWTError
from fastapi import HTTPException, status
from datetime import timedelta, datetime, timezone
from get_health_data import get_health_data
from create_heath_status import create_health_item
import pytest
from interfaces import HealthInfoBase, HealthStatuses
from protected_route import protected_route


class TestCreateAccessToken:
    def test_create_access_token_without_expires_delta(self):
        data = {"user_id": 123}
        token = create_access_token(data)
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert decoded_data["user_id"] == data["user_id"]

    def test_create_access_token_with_expires_delta(self):
        data = {"user_id": 123}
        expires_delta = timedelta(minutes=30)
        token = create_access_token(data, expires_delta=expires_delta)
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert decoded_data["user_id"] == data["user_id"]
        assert decoded_data["exp"] != datetime.now(timezone.utc) + expires_delta

    def test_create_access_token_with_custom_expires_delta(self):
        data = {"user_id": 123}
        expires_delta = timedelta(days=1)
        token = create_access_token(data, expires_delta=expires_delta)
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert decoded_data["user_id"] == data["user_id"]
        assert decoded_data["exp"] != datetime.now(timezone.utc) + expires_delta


class TestVerifyPassword:
    def test_correct_password(self):
        user_password = pwd_context.hash("password123")
        assert verify_password("password123", user_password) == True

    def test_incorrect_password(self):
        user_password = pwd_context.hash("password123")
        assert verify_password("wrong password", user_password) == False


class TestGetUser:
    def test_existing_user(self):
        db = {
            "user1": {"username": "user1", "email": "user1@example.com"},
            "user2": {"username": "user2", "email": "user2@example.com"},
        }
        username = "user1"
        user = get_user(db, username)
        assert user.username == "user1"
        assert user.email == "user1@example.com"

    def test_non_existing_user(self):
        db = {
            "user1": {"username": "user1", "email": "user1@example.com"},
            "user2": {"username": "user2", "email": "user2@example.com"},
        }
        username = "non_existing_user"
        user = get_user(db, username)
        assert user is None


class TestAuthenticateUser:
    def test_correct_credentials(self):
        fake_db = {
            "user1": {
                "username": "user1",
                "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
            "user2": {
                "username": "user2",
                "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
        }
        username = "user1"
        password = "secret"
        user = authenticate_user(fake_db, username, password)
        assert True

    def test_incorrect_username(self):
        fake_db = {
            "user1": {
                "username": "user1",
                "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
            "user2": {
                "username": "user2",
                "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
        }
        username = "non_existing_user"
        password = "secret"
        user = authenticate_user(fake_db, username, password)
        assert user == False

    def test_incorrect_password(self):
        fake_db = {
            "user1": {
                "username": "user1",
                "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
            "user2": {
                "username": "user2",
                "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
        }
        username = "user1"
        password = "wrong_password"
        user = authenticate_user(fake_db, username, password)
        assert user == False

    def test_empty_fake_db(self):
        fake_db = {}
        username = "user1"
        password = "password1"
        user = authenticate_user(fake_db, username, password)
        assert user == False


@pytest.mark.asyncio
class TestGetHealthData:
    async def test_get_health_data_returns_data(self):
        result = await get_health_data()
        data = result["data"]
        assert isinstance(result, dict)
        assert "data" in result
        assert isinstance(data, list)


@pytest.mark.asyncio
class TestCreateHealthItem:
    async def test_create_health_item_returns_data(self):
        mock_health_info_base = HealthInfoBase(
            name="Test Health Item", status=HealthStatuses.GOOD
        )

        response = await create_health_item(mock_health_info_base)

        assert isinstance(response, dict)
        assert "id" in response
        assert "name" in response
        assert "status" in response
        assert response["name"] == mock_health_info_base.name
        assert "status" in response
        assert response["status"] == mock_health_info_base.status


@pytest.mark.asyncio
class TestProtectedRoute:
    async def test_valid_token(self, monkeypatch):
        valid_token = "valid_token"
        fake_user = {"username": "test_user"}

        def mock_decode(token, *args, **kwargs):
            return {"sub": fake_user["username"]}

        monkeypatch.setattr("protected_route.jwt.decode", mock_decode)

        def mock_get_user(users, username):
            return fake_user

        monkeypatch.setattr("protected_route.get_user", mock_get_user)

        user = await protected_route(valid_token)

        assert user == fake_user

    async def test_invalid_token(self, monkeypatch):
        invalid_token = "invalid_token"

        def mock_decode(token, *args, **kwargs):
            raise JWTError("Invalid token")

        monkeypatch.setattr("protected_route.jwt.decode", mock_decode)

        with pytest.raises(HTTPException) as exc_info:
            await protected_route(invalid_token)

        assert exc_info.type == HTTPException
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
