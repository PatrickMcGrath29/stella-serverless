import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from src.api import AliasAPI

app = Flask(__name__)
CORS(app)

app.config["MONGODB_SETTINGS"] = {"host": os.environ["CONNECTION_STRING"]}
db = MongoEngine(app)

app.config["WTF_CSRF_ENABLED"] = False

alias_view = AliasAPI.as_view("alias_api")
app.add_url_rule("/alias/<string:name>", view_func=alias_view, methods=["GET"], endpoint="alias.read")
app.add_url_rule("/alias/", view_func=alias_view, methods=["POST", "DELETE"], endpoint="alias.write")
