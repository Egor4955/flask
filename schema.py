import pydantic
from abc import ABC


class AbstractAdvert(pydantic.BaseModel, ABC):
    title: str
    description: str
    owner: str


class CreateAdvert(AbstractAdvert):
    title: str
    description: str
    owner: str


class UpdateAdvert(AbstractAdvert):
    title: str
    description: str
    owner: str