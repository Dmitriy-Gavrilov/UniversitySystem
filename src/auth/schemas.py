from src.base.schemas import BaseSchema
from src.user.models import UserRole


class AuthSchema(BaseSchema):
    login: str
    password: str
    role: UserRole


class AuthResponseSchema(BaseSchema):
    access_token: str
