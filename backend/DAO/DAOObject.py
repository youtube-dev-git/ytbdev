from ..videos_fetcher.classes.syllabus import Syllabus
from ..APIs.user import User, Learner, Admin, Expert
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
    def read_syllabus_videos (self) -> Syllabus :
        pass
    
    # @classmethod
    # def save_expert(e:Expert) -> None :
    #     pass  
      
    # @classmethod
    # def save_learner(e:Learner) -> None :
    #     pass    
    
    # @classmethod
    # def save_admin(e:Admin) -> None :
    #     pass
    
    @classmethod
    def connect_user(mail : str, password: str) -> User :
        pass
    
class DAOAdmin:
    
    def save(self, admin: Admin) -> Admin:
        # Instructions
        pass

class DAOLearner:
    
    def save(self, learner : Learner) -> Learner:
        # Instructions
        pass
    
class DAOExpert(DAOLearner):
    
    def save(self, expert : Expert) -> Expert:
        super().save()
        # Autres instructions 
        pass