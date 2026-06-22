from pydantic import BaseModel
from typing import Optional

# This schema defines what the user sends us when creating a task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "Medium"  # Low, Medium, High

# This schema is what we send BACK to the user (includes AI suggestions)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    ai_time_estimate: str
    ai_study_tip: str
