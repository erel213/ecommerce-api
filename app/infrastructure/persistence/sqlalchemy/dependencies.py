from sqlalchemy.orm import Session
from app.infrastructure.persistence.sqlalchemy.session import DatabaseSessionSingleton

def get_db():
    db_manager= DatabaseSessionSingleton()
    db = db_manager.get_session()
    try:
        yield db
    finally:
        db.close()