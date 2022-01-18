

from typing import Any, List
from pydantic.main import BaseModel
from ..Permanent_Classes.syllabus import Syllabus

class PrimarySyllabus(BaseModel):
    title : str
    lessons: List
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def syllabusConversion(self) -> Syllabus:
        syllabus = Syllabus(title = self.title)
        for lesson in self.lessons :
            syllabus.appendLesson(lesson)
        return syllabus


# dico = {
#     "title" : "john wick", 
#     "lessons" : ["1", "2", "parabellum"]
# }
# print(PrimarySyllabus(**dico).syllabusConversion())