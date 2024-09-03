from typing import Optional, List
from app.core.domain.entity.user import User

class UserRepository: 
    def get_user_by_id(self, user_id : int) -> Optional[User]:
        raise NotImplementedError

    def get_user_by_username(self, username : str) -> Optional[User]:
        raise NotImplementedError
    
    def create_user(self , user: User) -> User:
        raise NotImplementedError
    
    def update_user (self, user : User) -> User:
        raise NotImplementedError

    def list_users(self) -> List[User]:
        raise NotImplementedError


