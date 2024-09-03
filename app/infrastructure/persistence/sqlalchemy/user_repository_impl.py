from sqlalchemy.orm import Session
from typing import Optional, List
from app.core.domain.entity.user import User
from app.core.domain.repository.user_repository import UserRepository
from app.infrastructure.persistence.sqlalchemy.models import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db : Session):
        self.db = db
    
    def get_user_by_id(self, user_id: int) ->  Optional[User]:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            return User(
                id=user.id,
                username=user.username,
                email=user.email,
                hashed_password=user.hashed_password,
                is_active=user.is_active
            )

        return None
    
    def create_user(self, user: User) -> User:
        user_model = UserModel(
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            is_active=user.is_active
        )

        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return User(
            id=user_model.id,
            username=user_model.username,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
            is_active=user_model.is_active
            )
        