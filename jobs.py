import asyncio
import uuid

# In-memory job store
jobs = {}

async def process_job(job_id: str, doc_content: str):
    """Simulate async processing for 2-3 seconds"""
    jobs[job_id]['status'] = 'processing'
    await asyncio.sleep(2 + 1)  # Simulate processing delay
    jobs[job_id]['status'] = 'completed'
    jobs[job_id]['result'] = f"Processed content length: {len(doc_content)}"
