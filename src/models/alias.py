import secrets

from mongoengine import Document, StringField, URLField
from pydantic import AnyHttpUrl, BaseModel


class Alias(Document):
    name = StringField(required=True, unique=True)
    url = URLField(schemes=["http", "https"], required=True)
    secret_key = StringField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        self.secret_key = secrets.token_urlsafe()


class AliasData(BaseModel):
    name: str
    url: AnyHttpUrl

    class Config:
        orm_mode = True
