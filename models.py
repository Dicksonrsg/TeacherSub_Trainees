from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class Phone(str):
    number: str

class Pedagog(BaseModel):
    id: Optional[str]
    first_name: str
    surname: str
    password: str

class Teacher(BaseModel):
    id: Optional[str]
    first_name: str
    surname: str
    password: str
    phones: Optional[List[Phone]]
