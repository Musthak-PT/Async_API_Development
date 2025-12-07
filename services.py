import asyncio
import uuid
from models import jobs, JobStatus

async def process_document(job_id: str):
    try:
        jobs[job_id] = JobStatus.processing
        await asyncio.sleep(3)  # Simulate async processing delay
        jobs[job_id] = JobStatus.completed
    except Exception as e:
        jobs[job_id] = JobStatus.failed
