from typing import List
from Permanent_Classes.syllabus import Syllabus
from Permanent_Classes.users import User, Learner, Admin, Expert


class DAOObject:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def save_syllabus(self,expert_id: int,syllabus : Syllabus) -> int :
        # Cette fonction renvoie l'identifiant en BD du syllabus qui a été stocké
        pass
    
    @classmethod
    def save_syllabus_videos(self, syllabus : Syllabus, syllabus_id: int) -> None :
        # Cette fonction prend en paramètre un syllabus muni de ses vidéos et actualise
        # de fait le syllabus d'id syllabus_id
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