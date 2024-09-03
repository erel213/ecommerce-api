from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , Session
from app.core.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

# Create a Base class for declarative class definitions
Base = declarative_base()

class DatabaseSessionSingleton:
    _instance = None
    _session_factory = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSessionSingleton, cls).__new__(cls)
            cls._initialize_session()
        return cls._instance

    @classmethod
    def _initialize_session(cls):
        engine = create_engine(DATABASE_URL)
        cls._session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_session(self) -> Session:
        return self._session_factory()  # Return a new session instance

