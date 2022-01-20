# from Permanent_Classes.lesson import Lesson
from googleapiclient.discovery import build


class YoutubeAPIHandler :
    API_NAME = "youtube"
    API_VERSION = "v3"
    API_KEY = "AIzaSyCczWd9sOMfJOKEcbYhneIS_UzrY4dOGuo"
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    
    def __init__(self) -> None:
        pass
    
    # from Permanent_Classes.syllabus import Syllabus
    @classmethod
    def fetch_by_query(self, syllabus ):
        for lesson in syllabus.lessons:
            videos = self.__search_by_query(lesson.title)
            lesson.appendVideos(videos)
        
     
    @classmethod
    def __search_by_query(self, query : str) -> dict:
        request = self.youtube.search().list(
            # part='statistics,snippet',
            part='snippet',
            maxResults = 25,
            q = query,
            fields = "items(id,snippet(channelId, title,description,publishedAt,thumbnails/medium/url))"
            # fields = "items(id,snippet(channelId, title,description,publishedAt,thumbnails/medium/url), statistics(viewCount))"
        )
        response = request.execute()
        # print(response)
        return response
    
    @classmethod
    def _get_view_count(self, video_id : str) -> int:
        request = self.youtube.videos().list(
            part="statistics",
            id=video_id,
            fields = "items(statistics(viewCount))"
        )
        response = request.execute()
        return int(response["items"]["statistics"]["viewCount"])