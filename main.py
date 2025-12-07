from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from schemas import UploadRequest, UploadResponse, ProcessResponse, StatusResponse
from services import process_document
from models import jobs, JobStatus
import uuid

app = FastAPI(title="Async API Demo")

# -------------------------------
# Class-based API
# -------------------------------

class DocumentAPI:
    @staticmethod
    async def upload_document(request: UploadRequest, background_tasks: BackgroundTasks):
        # Generate job ID
        job_id = str(uuid.uuid4())
        jobs[job_id] = JobStatus.pending
        
        # Add background task
        background_tasks.add_task(process_document, job_id)
        
        return JSONResponse(
            status_code=201,
            content={"job_id": job_id, "status": "pending"}
        )

    @staticmethod
    async def get_status(job_id: str):
        if job_id not in jobs:
            raise HTTPException(status_code=404, detail="Job ID not found")
        
        return JSONResponse(
            status_code=200,
            content={"job_id": job_id, "status": jobs[job_id]}
        )

    @staticmethod
    async def process_job():
        # For demonstration, just return success immediately
        return JSONResponse(
            status_code=200,
            content={"message": "Processing started asynchronously", "status": "success"}
        )

# -------------------------------
# Routes
# -------------------------------
from fastapi import Depends

@app.post("/upload", response_model=UploadResponse)
async def upload(request: UploadRequest, background_tasks: BackgroundTasks):
    return await DocumentAPI.upload_document(request, background_tasks)

@app.get("/status/{job_id}", response_model=StatusResponse)
async def status(job_id: str):
    return await DocumentAPI.get_status(job_id)

@app.post("/process", response_model=ProcessResponse)
async def process():
    return await DocumentAPI.process_job()
