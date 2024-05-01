from fastapi import Depends, APIRouter
import uuid
from interfaces import HealthInfoBase, HealthInfo
from protected_route import protected_route


create_heath_status_router = APIRouter()


@create_heath_status_router.post(
    "/status/",
    response_model=HealthInfo,
    dependencies=[Depends(protected_route)],
)
async def create_health_item(
    healthInfo: HealthInfoBase,
) -> HealthInfoBase:
    return {**healthInfo.model_dump(), "id": uuid.uuid4()}
