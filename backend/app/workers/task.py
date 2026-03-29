from .celery_app import celery
from ..database import SessionLocal
from ..models import Document
from ..utils.redis_client import redis_client
import time

@celery.task(bind=True)
def process_document(self, doc_id):
    db = SessionLocal()
    doc = db.query(Document).get(doc_id)

    steps = [
        ("parsing", 20),
        ("extracting", 50),
        ("finalizing", 80),
        ("completed", 100)
    ]

    for step, progress in steps:
        doc.status = step
        doc.progress = progress
        db.commit()
        redis_client.publish(f"doc_{doc_id}", progress)
        time.sleep(2)

    doc.result = {
        "summary": "Processed successfully",
        "keywords": ["AI", "Docs"]
    }

    doc.status = "completed"
    doc.progress = 100
    db.commit()
