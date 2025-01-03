from sqlalchemy import Column, String, Boolean
from app.db.base import Base


class User(Base):
    name = Column(String(length=128), nullable=True)
    email = Column(String(length=128), unique=True, nullable=False, index=True)
    password = Column(String(length=32), nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
