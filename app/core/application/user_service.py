from typing import List
from app.core.domain.repository.user_repository import UserRepository
from app.core.application.dtos.user_dto import UserDto
from app.core.domain.entity.user import User

class UserService:
    def __init__(self, user_repository : UserRepository):
        self.user_repository=user_repository
    
    def get_user_by_id(self, username: str) -> UserDto:
        user = self.user_repository.get_user_by_username(username=username)
        return UserDto.from_entity(user)
    
    def get_user_by_username (self, user_id: int) -> UserDto:
        user = self.user_repository.get_user_by_id(user_id=user_id)
        return UserDto.from_entity(user)
    
    def create_user(self, user_data: UserDto) -> UserDto:
        new_user= User(
            id=0,
            username=user_data.username,
            email=user_data.email,
            hashed_password=user_data.hashed_password,
            is_active=user_data.is_active
        )

        created_user = self.user_repository.create_user(user=new_user)
        return UserDto.from_entity(created_user)

    def update_user(self, user_data: UserDto) -> UserDto:
        user_to_updae = self.user_repository.get_user_by_id(user_id=user_data.id)
        if user_to_updae:
            user_to_updae.username = user_data.username
            user_to_updae.email = user_data.email
            user_to_updae.hashed_password = user_data.hashed_password
            user_to_updae.is_active = user_data.is_active
            updated_user = self.user_repository.update_user(user=user_to_updae)
            return UserDto.from_entity(updated_user)
        return None
    
    def list_users(self) -> List[UserDto]:
        users = self.user_repository.list_users()
        return [UserDto.from_entity(user) for user in users]
    
