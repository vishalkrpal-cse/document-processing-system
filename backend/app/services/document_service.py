from ..database import SessionLocal
from ..models import Document

def create_document(filename):
    db = SessionLocal()

    doc = Document(filename=filename, status="uploaded")
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return doc
