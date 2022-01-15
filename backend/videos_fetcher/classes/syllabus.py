from typing import Any, List, Optional

from pydantic.main import BaseModel
from lesson import Lesson

class Syllabus(BaseModel):
    title: str
    lessons: Optional[List]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    def appendLesson(self, lessonTitle : str) -> None:
        if self.lessons == None :
            self.lessons = []
        self.lessons.append(Lesson(title = lessonTitle))
        

    
syllabus = Syllabus(title = "1")