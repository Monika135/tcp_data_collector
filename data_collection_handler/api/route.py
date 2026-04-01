from flask import Blueprint
from flask_restx import Api
from .api_handler.api_handler import HealthCheck, DeviceRecords

v1_blueprint = Blueprint("v1", __name__)

v1_api = Api(
    v1_blueprint,
    prefix="/v1",
    title="Device records",
    version="1.0",
    description="Device records API's",
    doc="/apidocs/",
)

v1_api.add_resource(HealthCheck, "/health_check/")
v1_api.add_resource(DeviceRecords, "/api/device_record/")