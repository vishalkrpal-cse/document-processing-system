from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    status = Column(String)
    progress = Column(Integer, default=0)
    result = Column(JSON, nullable=True)
