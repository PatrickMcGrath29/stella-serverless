import os

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)

app.config["MONGODB_SETTINGS"] = {"host": os.environ["CONNECTION_STRING"]}

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["WTF_CSRF_ENABLED"] = False
