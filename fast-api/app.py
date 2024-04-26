from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get_health_data import get_health_data_router
from create_heath_status import create_heath_status_router
from login import login_router
from interfaces import OpenApiSettings

open_api_settings = OpenApiSettings()
app = FastAPI(openapi_url=open_api_settings.openapi_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(get_health_data_router)
app.include_router(create_heath_status_router)
app.include_router(login_router)
