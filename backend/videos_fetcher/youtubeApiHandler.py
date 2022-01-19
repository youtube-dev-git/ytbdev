from ..Permanent_Classes.syllabus import Syllabus
from ..Permanent_Classes.lesson import Lesson
from googleapiclient.discovery import build

class YoutubeAPIHandler :
    API_NAME = "youtube"
    API_VERSION = "v3"
    API_KEY = ""
    
    def __init__(self) -> None:
        pass
    
    def fetch_by_query(self, syllabus : Syllabus) -> dict:
        for lesson in syllabus.lessons:
            videos = self.__search_by_query(syllabus.title + " " + lesson.title)
            lesson.appendVideos(videos)
            
     
    def __search_by_query(self, query : str) -> dict:
        youtube = build(self.API_NAME, self.API_VERSION, developerKey=self.API_KEY)
        request = youtube.search().list(
            part='statistics,snippet',
            maxResults = 25,
            q = query,
            fields = "items(id,snippet(channelId, title,description,publishedAt,thumbnails/medium/url), statistics(viewCount))"
        )
        response = request.execute()
        return response