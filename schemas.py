from pydantic import BaseModel, Field
from typing import Optional

class UploadRequest(BaseModel):
    document_type: str = Field(..., example="invoice")
    content: str = Field(..., example="Invoice #1234 details")

class UploadResponse(BaseModel):
    job_id: str
    status: str

class ProcessResponse(BaseModel):
    message: str
    status: str

class StatusResponse(BaseModel):
    job_id: str
    status: str
