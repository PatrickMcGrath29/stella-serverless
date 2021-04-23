import json
from dataclasses import dataclass
from enum import Enum

from pydantic import ValidationError

from src.alias import Alias


def create(event, context):
    params = _params_from_event(event, ['short_name', 'full_url'])
    short_name = params['short_name']
    full_url = params['full_url']

    try:
        alias = Alias(short_name=short_name, full_url=full_url)
    except ValidationError as exc:
        return HttpResponse(HttpStatusCode.BAD_REQUEST, exc.errors()).as_json

    return HttpResponse(HttpStatusCode.OK, alias.dict()).as_json


def get(event, context):
    print("get")
    print(event)

    return HttpResponse(HttpStatusCode.OK, {"message": "success"}).as_json


def delete(event, context):
    print("delete")
    print(event)

    return HttpResponse(HttpStatusCode.OK, {"message": "success"}).as_json


def _params_from_event(event: dict, fields: list):
    body_json = json.loads(event['body'])

    return {
        field: body_json[field]
        for field in fields
        if field in body_json
    }


class HttpStatusCode(Enum):
    OK = 200
    NOT_FOUND = 404
    BAD_REQUEST = 400


@dataclass
class HttpResponse:
    status_code: HttpStatusCode
    body: dict

    @property
    def as_json(self):
        wrapped_body = {
            'statusCode': self.status_code.value,
            'body': self.body
        }

        return {
            'statusCode': self.status_code.value,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(wrapped_body)
        }
