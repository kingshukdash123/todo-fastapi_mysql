from pydantic import Field, BaseModel
from typing import Annotated, Literal, Optional

class CreateTask(BaseModel):
    title: Annotated[str, Field(..., description='Title of the task')]
    description: Annotated[Optional[str], Field(description='Description of the task')] = None
    status: Annotated[Literal['pending','in_progress','completed'], Field(..., description='Status of the task')]

class UpdateTask(BaseModel):
    title: Annotated[Optional[str], Field(description='Title of the task')] = None
    description: Annotated[Optional[str], Field(description='Description of the task')] = None
    status: Annotated[Optional[Literal['pending','in_progress','completed']], Field(description='Status of the task')] = None