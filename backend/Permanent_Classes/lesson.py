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
        for video in videosJSON["items"]:
            self.videos.append(Video(**YoutubeAPIHandler._format_query(video)))
