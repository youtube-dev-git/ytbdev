from typing import Any, List

from pydantic.main import BaseModel
from .lesson import Lesson

class Syllabus(BaseModel):
    title: str
    lessons: List[Lesson]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
