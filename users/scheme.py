import logging
from typing import List, Optional

from ninja import Schema, UploadedFile, File

logger = logging.getLogger("debug")


class LoginInputSchema(Schema):
    username: str
    password: str


class LoginOutSchema(Schema):
    token: str


class PostAuthorSchema(Schema):
    username: str
    last_name: str
    first_name: str


class CountrySchema(Schema):
    id: int
    name: str


class CitySchema(Schema):
    id: int
    name: str


class UserProfileSchema(Schema):
    id: int
    username: str
    last_name: str
    first_name: str
    photo: str
    country: CountrySchema
    city: List[CitySchema]


class UserInputSchema(Schema):
    username: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    photo: Optional[File[UploadedFile]] = None
    country: Optional[int] = None
    city: Optional[List[int]] = None

    @staticmethod
    def resolve_city(obj):
        if obj["city"]:
            return obj["city"][0].replace(" ", "").split(",")
