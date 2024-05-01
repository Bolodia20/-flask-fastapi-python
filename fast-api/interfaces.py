import uuid
from enum import Enum
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import List, TypedDict, Dict


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


HealthInfoList = List[HealthInfo]

HealthInfoListResponse = TypedDict("HealthInfoListResponse", {"data": HealthInfoList})


class User(BaseModel):
    username: str
    full_name: str | None = None
    email: str | None = None
    password: str | None = None


FakeUsers = Dict[str, User]


class Token(BaseModel):
    access_token: str
    token_type: str


class OpenApiSettings(BaseSettings):
    openapi_url: str = "/openapi.json"
