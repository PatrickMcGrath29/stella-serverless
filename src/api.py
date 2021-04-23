import json
from dataclasses import dataclass
from enum import Enum

from pydantic import ValidationError

from src.alias import Alias


def create(event, context):
    print("create")
    print(event)
    short_name = 'hello'
    full_url = 'https://patrickmcgrath.io'

    try:
        alias = Alias(short_name=short_name, full_url=full_url)
    except ValidationError as exc:
        return HttpResponse(HttpStatusCode.BAD_REQUEST, exc.json())

    return HttpResponse(HttpStatusCode.OK, {"message": "success"}).as_json


def get(event, context):
    print("get")
    print(event)

    return HttpResponse(HttpStatusCode.OK, {"message": "success"}).as_json


def delete(event, context):
    print("delete")
    print(event)

    return HttpResponse(HttpStatusCode.OK, {"message": "success"}).as_json


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
        return {
            'statusCode': self.status_code.value,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(self.body),
        }
