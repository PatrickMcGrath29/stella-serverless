import os
import secrets

from pydantic import HttpUrl, PrivateAttr, SecretStr

from src.utils.dynamo_client import DynamoModel


class Alias(DynamoModel):
    short_name: str
    full_url: HttpUrl
    _secret_key: SecretStr = PrivateAttr()

    def __init__(self, **data: dict) -> None:
        super().__init__(**data)
        self._secret_key = SecretStr(secrets.token_urlsafe())

    def dict_with_secret_key(self) -> dict:
        alias_dict = self.dict()
        alias_dict['secret_key'] = self._secret_key.get_secret_value()

        return alias_dict

    @property
    def table_name(self):
        return os.environ['STELLA_DYNAMODB_TABLE']

    def to_dynamo(self):
        return {
            'short_name': {'S': self.short_name},
            'full_url': {'S': str(self.full_url)}
        }

    def from_dynamo(self):
        pass
