from fastapi import APIRouter
from ..database import SessionLocal
from ..models import Document

router = APIRouter()

@router.get("/documents")
def get_docs():
    db = SessionLocal()
    return db.query(Document).all()
