from googleapiclient.discovery import build


class YoutubeAPIHandler :
    API_NAME = "youtube"
    API_VERSION = "v3"
    API_KEY = "AIzaSyCczWd9sOMfJOKEcbYhneIS_UzrY4dOGuo"
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    def __init__(self) -> None:
        pass
    
    @classmethod
    def fetch_by_query(self, syllabus ):
        for lesson in syllabus.lessons:
            videos = self.__search_by_query(lesson.title)
            lesson.appendVideos(videos)
        
     
    @classmethod
    def __search_by_query(self, query : str) -> dict:
        request = self.youtube.search().list(
            part='snippet',
            maxResults = 25,
            q = query,
            type="video"
        )
        response = request.execute()
        return response
    
    @classmethod
    def _get_view_count(self, video_id : str) -> int:
        request = self.youtube.videos().list(
            part="statistics",
            id=video_id,
            fields = "items(statistics(viewCount))"
        )
        response = request.execute()
        return int(response["items"][0]["statistics"]["viewCount"])
    
    @classmethod
    def _format_query(self, video : dict) -> dict:
        print(video)
        return {
            "video_id" : video["id"]["videoId"],
            "title" : video["snippet"]["title"],
            "viewCount" : YoutubeAPIHandler._get_view_count(video["id"]["videoId"]),
            "description" : video["snippet"]["description"],
            "published_at" : video["snippet"]["publishedAt"],
            "thumbnails_medium" : video["snippet"]["thumbnails"]["medium"]["url"],
            "channel_id" : video["snippet"]["channelId"],
        }