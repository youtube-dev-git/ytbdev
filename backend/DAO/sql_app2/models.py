from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Syllabus(Base):
    __tablename__ = "syllabus"

    id=Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description= Column(String, unique=True, index=True)

    video= relationship("Video", back_populates="owner")

    
class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    viewCount = Column(Integer, index=True)
    description = Column(String(150), index=True)
    publishedAt = Column(String(50), index=True)
    thumbnails = Column(String(50), index=True)
    channel_id = Column(String(50), index=True)
    owner_id = Column(Integer, ForeignKey("syllabus.id"))

    owner= relationship("Syllabus", back_populates="video")