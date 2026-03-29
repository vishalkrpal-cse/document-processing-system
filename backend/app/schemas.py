from pydantic import BaseModel

class DocumentResponse(BaseModel):
    id: int
    filename: str
    status: str
    progress: int

    class Config:
        from_attributes = True
