from typing import Optional

from ninja import Schema


class LoginInputSchema(Schema):
    username: str
    password: str


class LoginOutSchema(Schema):
    token: str


class PostAuthorSchema(Schema):
    username: str
    last_name: str
    first_name: str


class UserProfileSchema(Schema):
    id: int
    username: str
    last_name: str
    first_name: str
    photo: str


class UserInputSchema(Schema):
    username: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
