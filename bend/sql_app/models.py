from sqlalchemy import  Column, Integer, String
from .database import Base


class Lectures(Base):
    __tablename__ = "lectures"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)