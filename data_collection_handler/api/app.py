from flask import Flask, jsonify
from flask_cors import CORS
from .route import v1_blueprint

def create_app():
    app = Flask(__name__)
    CORS(
        app,
        resources={r"/*": {"origins": "*", "send_wildcard": "False"}},
    )
    CORS(app)
    app.register_blueprint(v1_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()