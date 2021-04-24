import secrets

from pydantic import AnyUrl, BaseModel, PrivateAttr, SecretStr


class Alias(BaseModel):
    short_name: str
    full_url: AnyUrl
    _secret_key: SecretStr = PrivateAttr()

    def __init__(self, **data: dict) -> None:
        super().__init__(**data)
        self._secret_key = SecretStr(secrets.token_urlsafe())

    def dict_with_secret_key(self) -> dict:
        alias_dict = self.dict()
        alias_dict['secret_key'] = self._secret_key.get_secret_value()

        return alias_dict
