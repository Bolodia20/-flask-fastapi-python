from fastapi import APIRouter
from mock_up_data import mock_up_health_data
from interfaces import HealthInfoListResponse

get_health_data_router = APIRouter()


@get_health_data_router.get("/health/")
async def get_health_data() -> HealthInfoListResponse:
    return {"data": mock_up_health_data}
