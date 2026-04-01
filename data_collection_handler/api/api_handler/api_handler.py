from ..resource import APIResource
import logging
from flask_restx import Namespace
from .parser_handler import device_query_parser
from .schema import device_record_list

api = Namespace('Devices', description='Device operations')


class DeviceRecords(APIResource):
    @api.expect(device_query_parser)
    def get(self):
        try:
            request_data = device_query_parser.parse_args()
            device_id = request_data["device_id"]
            records = request_data["no_of_records"]
            if not device_id or not device_id.strip():
                return {
                    "message": "Device id is required",
                    "status": False,
                    "type": "custom_error"
                    }, 400

            if records is None or records <= 0:
                return {
                    "message": "no_of_records must be greater than 0",
                    "status": False,
                    "type": "custom_error"
                }, 400

            status, data = device_record_list(device_id, records)
            if status:
                return {
                    "message": "Device records fetched successfully",
                    "data": data,
                    "status": True,
                    "type": "success_message"
                    }, 200

            return {
                "message": data,
                "status": False,
                "type": "custom_error"
                }, 400

        except Exception as e:
            logging.error("DeviceRecords_error", exc_info=e)
            return {"message": "Something went wrong", "status": False,
                    "type": "custom_error"}, 400


class HealthCheck(APIResource):
    def get(self):
        try:
            return {"message": "SUCCESS"}, 200

        except Exception as e:
            logging.error("error in HealthCheck", exc_info=e)
            return {"message": 'error in health check'}, 400