from pydantic import Field, BaseModel
from typing import Annotated, Literal

class CreateTasks(BaseModel):
    title: Annotated[str, Field(..., description='Title of the task')]
    description: Annotated[str, Field(description='Description of the task')]
    status: Annotated[Literal['pending','in_progress','completed'], Field(..., description='Status of the task')]