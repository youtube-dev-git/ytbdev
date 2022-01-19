import imp
from youtubeApiHandler import YoutubeAPIHandler
from DAO.DAOObjects import DAOObject
from Permanent_Classes.syllabus import Syllabus


class System:
    def __init__(self) -> None:
        pass    
    
    @classmethod
    def save_syllabus(self,expert_id: int, syllabus : Syllabus):
        syllabus_db_id = DAOObject.save_syllabus(expert_id, syllabus)
        syllabus_videos_list = System.videos_syllabus_matching(syllabus)
        DAOObject.save_syllabus_videos(syllabus_videos_list, syllabus_db_id)
        
        
    @classmethod
    def videos_syllabus_matching(self, syllabus : Syllabus) -> Syllabus:
        return YoutubeAPIHandler.fetch_by_query(syllabus)
        
    @classmethod
    def all_syllabus_matching(self):
        pass
        