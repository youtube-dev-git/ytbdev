

from pydantic.main import BaseModel


class LessonVideo(BaseModel):
    videoId : str 
    viewCount: int
    channel_id : str 
    title : str 
    description : str 
    published_at : str 
    thumbnails_medium : str
    channel_title : str
    
    def __init__(self, **videoJSON : dict ) -> None:
        self.videoId = videoJSON["items"]["id"]
        self.title = videoJSON["items"]["snippet"]["title"]
        self.viewCount = videoJSON["items"]["statistics"]["viewCount"]
        self.channel_id = videoJSON["items"]["snippet"]["channelId"]
        self.description = videoJSON["items"]["snippet"]["description"]
        self.published_at = videoJSON["items"]["snippet"]["publishedAt"]
        self.thumbnails_medium = videoJSON["items"]["snippet"]["thumbnails"]["medium"]["url"]


print(LessonVideo(
    
))