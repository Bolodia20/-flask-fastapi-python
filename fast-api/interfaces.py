import uuid
from enum import Enum
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class HealthStatuses(str, Enum):
    GOOD = ("GOOD",)
    BAD = ("BAD",)
    NORMAL = ("NORMAL",)
    NONE = ("NONE",)


class HealthInfoBase(BaseModel):
    name: str
    status: HealthStatuses


class HealthInfo(HealthInfoBase):
    id: uuid.UUID


class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    password: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class OpenApiSettings(BaseSettings):
    openapi_url: str = "/openapi.json"
