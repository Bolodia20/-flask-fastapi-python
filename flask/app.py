from flask import Flask
from flask_cors import CORS
from get_health_status import get_health_data_router
from create_health_data import create_heath_status_router
from login import login_router
from consts import SECRET_KEY

app = Flask(__name__)

app.register_blueprint(get_health_data_router)
app.register_blueprint(create_heath_status_router)
app.register_blueprint(login_router)


app.config["SECRET_KEY"] = SECRET_KEY


CORS(app, support_credentials=True)
