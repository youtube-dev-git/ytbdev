from youtubeApiHandler import YoutubeAPIHandler
from syllabusGDBHandler import SyllabusGraphDBHandler


class System:
    def __init__(self) -> None:
        pass    
    
    def save_syllabus(self, syllabus : dict):
        SyllabusGraphDBHandler.save_syllabus(syllabus)
    
    def videos_syllabus_matching(self, syllabus : dict):
        syllabus_videos_list = YoutubeAPIHandler.fetch_by_query(syllabus)
        SyllabusGraphDBHandler.save_syllabus_videos(syllabus_videos_list)
        
    def all_syllabus_matching(self):
        pass
        