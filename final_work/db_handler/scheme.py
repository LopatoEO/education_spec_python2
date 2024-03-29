from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Model(Base):
    __tablename__ = 'cards'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_name = Column(String)
    card_code = Column(String)
    created_at = Column(TIMESTAMP, nullable=False)
