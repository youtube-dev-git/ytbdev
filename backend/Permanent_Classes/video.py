
from typing import Any
from pydantic.main import BaseModel


class Video(BaseModel):
    
    video_id : str 
    title : str
    viewCount: int
    description : str 
    published_at : str 
    thumbnails_medium : str
    channel_id : str
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
