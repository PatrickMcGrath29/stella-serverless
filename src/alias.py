from pydantic import AnyUrl, BaseModel


class Alias(BaseModel):
    short_name: str
    full_url: AnyUrl
