import os

from flask import Flask
from flask_mongoengine import MongoEngine

from src.api import AliasAPI

app = Flask(__name__)
db = MongoEngine(app)

app.config["MONGODB_SETTINGS"] = {"host": os.environ["CONNECTION_STRING"]}

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["WTF_CSRF_ENABLED"] = False

alias_view = AliasAPI.as_view("alias_api")
app.add_url_rule("/alias/<string:name>", view_func=alias_view, methods=["GET"])
app.add_url_rule("/alias/", view_func=alias_view, methods=["POST", "DELETE"])
