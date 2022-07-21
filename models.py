from calendar import WEDNESDAY
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Phone(str):
    number: str

class Time(str):
    time: str

class Day(str, Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    
class Available(BaseModel):
    day: Day
    shifts: List[Time]

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

#TODO: Add relatioship teacher->available
