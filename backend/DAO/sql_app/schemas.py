from os import stat
from typing import List, Optional
from pydantic import BaseModel


class AdminBase(BaseModel):
    email: str
    name: str
    photo: str
    gender: str
    phone: str
    
    statut = "admin"

class AdminCreate(AdminBase):
    password : str

class Admin(AdminBase):
    id: int
    is_active: bool
    #admin: List[Admin] = []
    #learners: List[Learner] = []
    
    class Config:
        orm_mode = True
            
class ExpertBase(BaseModel):
    email: str
    name: str
    photo: str
    gender: str
    phone: str
    
    statut = "expert"

class ExpertCreate(ExpertBase):
    password : str

class Expert(ExpertBase):
    id: int
    is_active: bool
    #expert: List[Expert] = []
    #learners: List[Learner] = []
    
    class Config:
        orm_mode = True

class LearnerBase(BaseModel):
    email: str
    name: str
    photo: str
    gender: str
    phone: str
    
    statut = "learner"

class LearnerCreate(LearnerBase):
    password : str

class Learner(LearnerBase):
    id: int
    is_active: bool
    #learner: List[Learner] = []
    #learners: List[Learner] = []
    
    class Config:
        orm_mode = True
