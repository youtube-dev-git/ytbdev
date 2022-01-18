from typing import List
from ..Permanent_Classes.syllabus import Syllabus
from ..Permanent_Classes.users import User, Learner, Admin, Expert
class DAOObject:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def save_syllabus(self, syllabus : Syllabus) -> None :
        pass
    
    @classmethod
    def save_syllabus_videos(self, syllabus : Syllabus) -> None :
        pass
    
    @classmethod
    def read_syllabus(self) -> Syllabus :
        pass
    
    @classmethod
    def list_trainings (self) -> List[Syllabus] :
        pass
    
    @classmethod
    def list_expert_trainings (self, expert_id) -> List[Syllabus] :
        pass
    
    @classmethod
    def connect_user(mail : str, password: str) -> User :
        pass
    
class DAOAdmin:
    
    def save(self, admin: Admin) -> Admin:
        pass

class DAOLearner:
    
    def save(self, learner : Learner) -> Learner:
        pass
    
class DAOExpert(DAOLearner):
    
    def save(self, expert : Expert) -> Expert:
        super().save()
        pass