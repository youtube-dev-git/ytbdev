
from typing import List, Optional

from pydantic import BaseModel



class VideoBase(BaseModel):
    Meta: str
    title: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int
    owner_id: int


class SyllabusBase(BaseModel):
    title: str


class SyllabusCreate(SyllabusBase):
    description: str
    


class Syllabus(SyllabusBase):
    id: int
    videos: List[Video] = []
    

    class Config:
        orm_mode = True
