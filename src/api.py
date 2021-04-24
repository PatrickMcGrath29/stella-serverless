from flask import Flask, make_response, request
from pydantic import ValidationError

from src.alias import Alias

app = Flask(__name__)


@app.route('/', methods=['POST'])
def create_alias():
    # TODO: Clean up validation logic
    request_json = request.get_json()
    if request_json is None or not all(key in request_json for key in ['short_name', 'full_url']):
        return make_response('Invalid Request', 400)

    short_name = request_json['short_name']
    full_url = request_json['full_url']

    try:
        alias = Alias(short_name=short_name, full_url=full_url)
    except ValidationError as exc:
        return make_response({"errors": exc.errors()}, 400)

    return make_response(alias.dict_with_secret_key(), 200)


@app.route('/<short_name>', methods=['GET'])
def get(short_name):
    return make_response({'message': 'success'}, 200)


@app.route('/<short_name>', methods=['DELETE'])
def delete(short_name):
    return make_response({'message': 'success'}, 200)
