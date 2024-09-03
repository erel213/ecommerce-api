from fastapi import APIRouter, Depends, HTTPException
from app.core.application.dtos.user_dto import UserDto
from sqlalchemy.orm import Session
from app.infrastructure.persistence.sqlalchemy.user_repository_impl import SQLAlchemyUserRepository
from app.core.application.user_service import UserService
from app.infrastructure.persistence.sqlalchemy.dependencies import get_db

router = APIRouter()

@router.post("/register", response_model=UserDto)
def register_user(user: UserDto, db: Session = Depends(get_db)):
    user_repository = SQLAlchemyUserRepository(db)
    user_service = UserService(user_repository=user_repository)
    return user_service.create_user(user_data=user)
