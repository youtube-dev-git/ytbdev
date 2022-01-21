from .youtubeApiHandler import YoutubeAPIHandler
from DAO.DAOObjects import MainDAO
from Permanent_Classes.syllabus import Syllabus


class System:
    def __init__(self) -> None:
        pass    
    
    @classmethod
    def save_and_build_syllabus(self,expert_id: int, syllabus : Syllabus):
        syllabus_db_id = MainDAO.save_syllabus(expert_id, syllabus)
        System.videos_syllabus_matching(syllabus)
        MainDAO.save_syllabus_videos(syllabus, syllabus_db_id)
        
        
    @classmethod
    def videos_syllabus_matching(self, syllabus : Syllabus) :
        YoutubeAPIHandler.fetch_by_query(syllabus)
        
    @classmethod
    def all_syllabus_matching(self):
        pass
        