import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.app import create_app
from dotenv import load_dotenv
import os
load_dotenv()

app = create_app()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///" + os.path.join(BASE_DIR, "devices.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")