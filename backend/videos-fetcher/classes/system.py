from youtubeApiHandler import YoutubeAPIHandler
from syllabusGraphDBHandler import SyllabusGraphDBHandler
from syllabus import Syllabus


class System:
    def __init__(self) -> None:
        pass    
    
    @classmethod
    def save_syllabus(self, syllabus : Syllabus):
        SyllabusGraphDBHandler.save_syllabus(syllabus)
        System.videos_syllabus_matching(syllabus)
        
    @classmethod
    def videos_syllabus_matching(self, syllabus : Syllabus):
        syllabus_videos_list = YoutubeAPIHandler.fetch_by_query(syllabus)
        SyllabusGraphDBHandler.save_syllabus_videos(syllabus_videos_list)
        
    @classmethod
    def all_syllabus_matching(self):
        pass
        