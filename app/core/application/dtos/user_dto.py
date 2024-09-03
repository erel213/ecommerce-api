from pydantic import BaseModel
from app.core.domain.entity.user import User
from typing import Optional

class UserDto(BaseModel):
    id : int
    username : str
    email : str
    hashed_password : str
    is_active : bool

    @staticmethod
    def from_entity(user : User):
        return UserDto(
            id=user.id,
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            is_active=user.is_active
        )