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
        key in request_json for key in ["short_name", "full_url"]
    ):
        return make_response({"errors": "invalid request"}, 400)

    short_name = request_json["short_name"]
    full_url = request_json["full_url"]

    try:
        alias = Alias(short_name=short_name, full_url=full_url)
        alias.save()
    except ValidationError as exc:
        return make_response({"errors": exc.errors()}, 400)
    except NotUniqueError:
        return make_response(
            {"errors": "an alias already exists with the given short_name"}, 400
        )

    return make_response(alias.serialize(include_secret_key=True), 200)


@app.route("/<short_name>", methods=["GET"])
def get(short_name):
    return make_response({"message": "success"}, 200)


@app.route("/<short_name>", methods=["DELETE"])
def delete(short_name):
    return make_response({"message": "success"}, 200)
