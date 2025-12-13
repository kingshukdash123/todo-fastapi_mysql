from pydantic import BaseModel, Field
from typing import Annotated


class CreateUser(BaseModel):
    name: Annotated[str, Field(..., description='Name of the user')]
    username: Annotated[str, Field(..., description='Unique username of the user')]
    password: Annotated[str, Field(..., description='Strong password')]


class LogInUser(BaseModel):
    username: Annotated[str, Field(..., description='Enter your username')]
    password: Annotated[str, Field(..., description='Enter your password')]