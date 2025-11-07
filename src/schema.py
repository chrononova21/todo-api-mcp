from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class StatusType(str, Enum):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

class PriorityType(str, Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

class Task(BaseModel):
    title: str
    description: str
    status: StatusType
    priority: PriorityType
    tags: Optional[List[str]]

class NewTaskResponse(BaseModel):
    task_id: str
    title: str
    priority: PriorityType

