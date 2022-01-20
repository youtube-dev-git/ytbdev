# from Permanent_Classes.lesson import Lesson
from googleapiclient.discovery import build

# import os

# import google_auth_oauthlib.flow
# import googleapiclient.discovery
# import googleapiclient.errors

class YoutubeAPIHandler :
    API_NAME = "youtube"
    API_VERSION = "v3"
    API_KEY = "AIzaSyCczWd9sOMfJOKEcbYhneIS_UzrY4dOGuo"
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    
    # scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    # api_service_name = "youtube"
    # api_version = "v3"
    # client_secrets_file = "code_secret_client_581014431912-9f5dn2495d01m9ir7c4d05mic3eceqnb.apps.googleusercontent.com.json"
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials)

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
            part='snippet',
            maxResults = 25,
            q = query
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
        return int(response["items"]["statistics"]["viewCount"])
    
    @classmethod
    def _format_query(self, video : dict) -> dict:
        print(video)
        return {
            "video_id" : video["id"]["videoId"],
            "title" : video["snippet"]["title"],
            "viewCount" : YoutubeAPIHandler._get_view_count(video["items"][0]["id"]),
            "description" : video["snippet"]["description"],
            "published_at" : video["snippet"]["publishedAt"],
            "thumbnails_medium" : video["snippet"]["thumbnails"]["medium"]["url"],
            "channel_id" : video["snippet"]["channelId"],
        }