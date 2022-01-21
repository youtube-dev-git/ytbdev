
from typing import List, Optional

from pydantic import BaseModel




class VideoBase(BaseModel):
    # videoID : str
    title : str
    viewCount : int
    description : str 
    publishedAt : str
    thumbnails : str
    channel_id : str

class VideoCreate(VideoBase):
    pass  

class Video(VideoBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True

class SyllabusBase(BaseModel):
    title: str


class SyllabusCreate(SyllabusBase):
    description: str
    


class Syllabus(SyllabusBase):
    id: int
    video: List[Video] = []
    

    class Config:
        orm_mode = True