from flask import Flask, make_response, request
from mongoengine import NotUniqueError
from pydantic import ValidationError

from src.models.alias import Alias

app = Flask(__name__)


@app.route("/", methods=["POST"])
def create_alias():
    # TODO: Clean up validation logic
    request_json = request.get_json()
    if request_json is None or not all(
        key in request_json for key in ["name", "full_url"]
    ):
        return make_response({"errors": "invalid request"}, 400)

    name = request_json["name"]
    full_url = request_json["full_url"]

    try:
        alias = Alias(name=name, full_url=full_url)
        alias.save()
    except ValidationError as exc:
        return make_response({"errors": exc.errors()}, 400)
    except NotUniqueError:
        return make_response(
            {"errors": "an alias already exists with the given name"}, 400
        )

    return make_response(alias.serialize(include_secret_key=True), 200)


@app.route("/<name>", methods=["GET"])
def get(name):
    return make_response({"message": "success"}, 200)


@app.route("/<name>", methods=["DELETE"])
def delete(name):
    return make_response({"message": "success"}, 200)
