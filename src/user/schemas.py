from src.base.schemas import BaseSchema, BaseModelSchema
from pydantic import Field

from .models import UserRole


class BaseUserSchema(BaseSchema):
    login: str = Field(max_length=50)
    password: str = Field(max_length=128)
    role: UserRole


class CreateUserSchema(BaseUserSchema):
    pass


class UserSchema(BaseUserSchema, BaseModelSchema):
    pass
