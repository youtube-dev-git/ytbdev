from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    pass
class AdminCreate(AdminBase):
    pass
class Admin(AdminBase):
    id: int
    users_id: int
    
    class Config:
        orm_mode = True
class ExpertBase(BaseModel):
    pass
class ExpertCreate(ExpertBase):
    pass
class Expert(ExpertBase):
    id: int
    learner_id: int
    
    class Config:
        orm_mode = True
class LearnerBase(BaseModel):
    pass
class LearnerCreate(LearnerBase):
    pass
class Learner(LearnerBase):
    id: int
    users_id: int
    Experts: List[Expert] = []
    
    class Config:
        orm_mode = True
class VideoBase(BaseModel):
    videoId : str
    title : str
    viewCount : int
    description : str 
    publishedAt : str
    thumbnails : str
    channelId : str
class VideoCreate(VideoBase):
    pass    
class Video(VideoBase):
    id: int
    lesson_id: int
    
    class Config:
        orm_mode = True
class LessonBase(BaseModel):
    title: str
class LessonCreate(LessonBase):
    pass
class Lesson(LessonBase):
    id: int
    syllabus_id: int
    videos: List[Video] = []
    class Config:
        orm_mode = True

class SyllabusBase(BaseModel):
    title: str
class SyllabusCreate(SyllabusBase):
    pass
class Syllabus(SyllabusBase):
    id: int
    lessons: List[Lesson] = []
    class Config:
        orm_mode = True
class UserBase(BaseModel):
    email: str
    name: str
    photo: str
    gender: str
    phone: str
    
class UserCreate(UserBase):
    password : str

class User(UserBase):
    id: int
    is_active: bool
    admin: List[Admin] = []
    learners: List[Learner] = []
    
    class Config:
        orm_mode = True


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
