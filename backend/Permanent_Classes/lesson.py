from typing import Any, List, Optional
from pydantic.main import BaseModel

from videos_fetcher.youtubeApiHandler import YoutubeAPIHandler
from .video import Video


class Lesson(BaseModel):
    title : str
    videos : Optional[List[Video]]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    def set_videos_list(self, videos_list):
        self.videos_list = videos_list
        
    def appendVideos(self, videosJSON : dict) -> None:
        for video in videosJSON:
            print(video)
            self.videos.append(Video(
                videoId = video["items"]["id"],
                title = video["items"]["snippet"]["title"],
                viewCount= YoutubeAPIHandler._get_view_count(video["items"]["id"]),
                description = video["items"]["snippet"]["description"],
                published_at = video["items"]["snippet"]["publishedAt"],
                thumbnails_medium = video["items"]["snippet"]["thumbnails"]["medium"]["url"],
                channel_id = video["items"]["snippet"]["channelId"]
            ))
        