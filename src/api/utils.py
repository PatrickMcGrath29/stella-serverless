from typing import Union

from flask import make_response


def json_response(response: Union[dict, str], status_code: int):
    return make_response(response, status_code, {"Content-Type": "application/json"})
