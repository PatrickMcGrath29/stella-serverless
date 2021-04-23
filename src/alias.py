from pydantic import AnyUrl
from pydantic.dataclasses import dataclass


@dataclass
class Alias:
    short_name: str
    full_url: AnyUrl
