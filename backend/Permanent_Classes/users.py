from lib2to3.pgen2.token import OP
from typing import Any, List, Optional
from pydantic import BaseModel
# from DAO.DAOObjects import DAOObject, DAOLearner, DAOExpert, DAOAdmin
from Permanent_Classes.syllabus import Syllabus

class User(BaseModel):
    statut : Optional[str]
    id: Optional[int]
    name : str
    email: str
    phone_num : int
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
        from DAO.DAOObjects import DAOAdmin
        return DAOAdmin.save(self)
        
class Learner(User):
    statut = "learner"
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        from DAO.DAOObjects import DAOLearner
        return DAOLearner.save(self)
        
class Expert(Learner):
    statut = "expert"
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        from DAO.DAOObjects import DAOExpert
        return DAOExpert.save(self)
    
    @property
    def my_trainings(self) -> List[Syllabus]:
        from DAO.DAOObjects import DAOObject
        return DAOObject.list_expert_trainings(self.id)

