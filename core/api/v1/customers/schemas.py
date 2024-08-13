from ninja import Schema


class AuthInSchema(Schema):
    phone: str
    email: str


class AuthOutSchema(Schema):
    message: str


class TokenOutSchema(Schema):
    token: str


class TokenInSchema(Schema):
    phone: str
    email: str
    code: str
