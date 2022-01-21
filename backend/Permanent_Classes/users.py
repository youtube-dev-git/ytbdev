from typing import Any, List, Optional
from pydantic import BaseModel
from Permanent_Classes.syllabus import Syllabus

class User(BaseModel):
    statut : Optional[str]
    id: Optional[int]
    name : str
    email: str
    phone_num : str
    password: str
    gender: str
    photo: Optional[str]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    def register(self):
        pass

class Admin(User):
    statut = "admin"
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        from DAO.DAOObjects import AdminDAO
        return AdminDAO.save(self)
        
class Learner(User):
    statut = "learner"
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        from DAO.DAOObjects import LearnerDAO
        return LearnerDAO.save(self)
        
class Expert(Learner):
    statut = "expert"
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        from DAO.DAOObjects import ExpertDAO
        return ExpertDAO.save(self)
    
    @property
    def my_trainings(self) -> List[Syllabus]:
        from DAO.DAOObjects import MainDAO
        return MainDAO.list_expert_trainings(self.id)

