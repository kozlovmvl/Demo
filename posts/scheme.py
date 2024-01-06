from ninja import Schema

from users.scheme import PostAuthorSchema


class PostOutSchema(Schema):
    id: int
    title: str
    text: str
    author: PostAuthorSchema


class PostInputSchema(Schema):
    title: str
    text: str


class ErrorSchema(Schema):
    name: str
    text: str
