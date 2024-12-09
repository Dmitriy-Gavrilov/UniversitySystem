from src.base.schemas import BaseCreateSchema, BaseModelSchema
from pydantic import Field

from models import UserRole


class BaseUserSchema:
    login: str = Field(max_length=50)
    password: str = Field(max_length=128)
    role: UserRole


class UserSchema(BaseModelSchema, BaseUserSchema):
    pass


class CreateUserSchema(BaseCreateSchema, BaseUserSchema):
    pass
