Requirements

Python 3.10+

Install dependencies:
    pip install -r requirements.txt


```

## Run locally
```
uvicorn main:app --reload
```
## API Endpoints

1. Upload Document
URL: <Base_url>/upload
Payload:(POST)
    {
    "document_type": "invoice",
    "content": "Invoice #1234 for customer ABC, amount $500"
    }

Response Example:
{
    "job_id": "d000d034-95e9-49cd-a603-785c444ee728",
    "status": "pending"
}


2. Check Job Status
URL: (GET) <base_url>/status/{job_id} 
Response Example: 
{
  "job_id": "b1f4b5d6-3a2f-4c99-abc1-1234567890ab",
  "status": "completed"
}


3. Process Job
URL: (POST) <base_url>/process
Response Example: 
{
  "message": "Processing started asynchronously",
  "status": "success"
}



Notes:
    - Only two fields are accepted for upload: document_type and content.

    - Jobs are processed asynchronously using FastAPI background tasks.

    - Job statuses are stored in memory (not persisted) and are mocked for demonstration.

    - The project uses class-based views (DocumentAPI) for structured endpoints.