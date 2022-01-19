from pydantic import BaseModel
from ..Permanent_Classes.users import User
from ..Permanent_Classes.syllabus import Syllabus

class TypeSyllabus(BaseModel):
    expert_id : int 
    syllabus : Syllabus
    

class TypeUser(BaseModel):
    status : str 
    user : User

