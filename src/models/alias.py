from typing import Any, Optional

from mongoengine import Document, StringField, URLField
from pydantic import AnyHttpUrl, BaseModel


class Alias(Document):
    name = StringField(required=True, unique=True)
    url = URLField(schemes=["http", "https"], required=True)
    secret_key = StringField()


class AliasData(BaseModel):
    name: str
    url: AnyHttpUrl

    class Config:
        orm_mode = True


class AliasDataCreated(AliasData):
    secret_key: str
