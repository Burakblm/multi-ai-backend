from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_engine(settings.SQL_ALCHEMY_DATABASE_URL)
            cls._instance.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
            cls._instance.Base = declarative_base()
        return cls._instance


db_instance = Database()


def get_db():
    db = db_instance.SessionLocal()
    try:
        yield db
    finally:
        db.close()
