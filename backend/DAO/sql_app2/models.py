from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Syllabus(Base):
    __tablename__ = "syllabus"

    id=Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description= Column(String, unique=True, index=True)

    lessons= relationship("Lesson", back_populates="owner")


class Lesson(Base):
    __tablename__ = "lessons"

    id= Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    owner_lesson_id = Column(Integer, ForeignKey("syllabus.id"))

    owner= relationship("Syllabus", back_populates="lessons")
    video=relationship("Video", back_populates="owner_video")


    
class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    title = Column(String(50), index=True)
    viewCount = Column(Integer, index=True)
    description = Column(String(150), index=True)
    published_at = Column(String(50), index=True)
    thumbnails_medium = Column(String(50), index=True)
    channel_id = Column(String(50), index=True)
    owner_video_id = Column(Integer, ForeignKey("lessons.id"))

    owner_video= relationship("Lesson", back_populates="video")







    