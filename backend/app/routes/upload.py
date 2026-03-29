from fastapi import APIRouter, UploadFile, File
from ..services.document_service import create_document
from ..workers.tasks import process_document

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    doc = create_document(file.filename)
    process_document.delay(doc.id)
    return {"id": doc.id}
