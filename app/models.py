from pydantic import BaseModel, Field
from typing import List

class AgentRequest(BaseModel):
    request: str = Field(
        min_length=10,
        max_length=500
    )


class TaskStatus(BaseModel):
    id: int
    name: str
    status: str


class AgentResponse(BaseModel):
    status: str
    request: str
    tasks: List[TaskStatus]
    document_path: str
    memory_entries: int
    execution_time: str


class ExecutionState(BaseModel):
    request: str
    tasks: List[TaskStatus]