from flask_restx import reqparse

device_query_parser = reqparse.RequestParser(bundle_errors=True)
device_query_parser.add_argument("device_id", type=str, required=True, location="args")
device_query_parser.add_argument("no_of_records", type=int, required=False,
                                 location="args", default=10)