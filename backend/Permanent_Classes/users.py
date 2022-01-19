from lib2to3.pgen2.token import OP
from typing import Any, List, Optional
from pydantic import BaseModel
from DAO.DAOObjects import DAOObject, DAOLearner, DAOExpert, DAOAdmin
from backend.Permanent_Classes.syllabus import Syllabus

class User(BaseModel):
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
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        return DAOAdmin().save(self)
        
class Learner(User):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        return DAOLearner().save(self)
        
class Expert(Learner):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        return DAOExpert().save(self)
    
    @property
    def my_trainings(self) -> List[Syllabus]:
        return DAOObject.list_expert_trainings(self.id)
        # pass

