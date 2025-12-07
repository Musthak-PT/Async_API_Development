from typing import Dict
from enum import Enum

class JobStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"

# In-memory "database" to store jobs
jobs: Dict[str, JobStatus] = {}
