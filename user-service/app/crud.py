from fastapi import Depends
from sqlalchemy.orm import Session

from app import models
from app.core.db import get_db


def create_user(db: Session = Depends(get_db)):
    pass