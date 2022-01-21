from typing import List
from Permanent_Classes.syllabus import Syllabus
from Permanent_Classes.users import User, Learner, Admin, Expert

from DAO.sql_app.main import DAOObjects
from DAO.sql_app.database import SessionLocal
# from .Permanent_Classes import users


class MainDAO:
    def __init__(self) -> None:
        ...
        
    @classmethod
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    @classmethod
    def save_syllabus(self,expert_id: int,syllabus : Syllabus) -> int :
        # Cette fonction renvoie l'identifiant en BD du syllabus qui a été stocké
        ...
    
    @classmethod
    def save_syllabus_videos(self, syllabus : Syllabus, syllabus_id: int) -> None :
        # Cette fonction prend en paramètre un syllabus muni de ses vidéos et actualise
        # de fait le syllabus d'id syllabus_id
        ...
    
    @classmethod
    def read_syllabus(self, syllabus_id: int) -> Syllabus :
        # Cette fonction retourne le syllabus dont l'identifiant est passé en paramètre (id)
        ...
    
    @classmethod
    def list_trainings (self) -> List[Syllabus] :
        # Cette fonction liste toutes les formations (syllabus accompagnés de leurs vidéos) 
        # présentes dans la base de données
        ...
    
    @classmethod
    def list_expert_trainings (self, expert_id : int) -> List[Syllabus] :
        # Cette fonction liste toutes les formations postées par l'expert dont l'id est donné en paramètre
        ...
    
    @classmethod
    def connect_user(self, mail : str, password: str) -> User :
        # Cette fonction vérifie si le mail et le password passé en paramètre
        # correspondent à un utilisateur enregistré dans l'une des tables admin, expert ou apprenant 
        # Si l'utilisateur est retrouvé dans l'une de ces tables, un objet du type correspondant 
        # est retourné avec son identifiant de base de données
        
        # NB: La vérification doit se faire dans l'ordre : admin, puis expert, puis apprenant
        DAOObjects.login_learners(mail,password,SessionLocal())
        ...
    
class AdminDAO:
    
    @classmethod
    def save(self, admin: Admin) -> Admin:
        # Cette fonction enregistre un administrateur en base de données
        ...

class LearnerDAO:
    
    @classmethod
    def save(self, learner : Learner) -> Learner:
        # Cette fonction enregistre un aprennant en base de données
        ...
    
class ExpertDAO(LearnerDAO):
    
    @classmethod
    def save(self, expert : Expert) -> Expert:
        # Cette fonction enregistre un expert en base de données
        ...