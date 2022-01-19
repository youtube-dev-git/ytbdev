 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
   # password = Column(String(50), unique=True, index=True)
    photo = Column(String)
    gender = Column(String)
    phone = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    admin = relationship("Admin", back_populates="user_A")   #1

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user_A= relationship("User", back_populates="admin ")   #1
    
class Learner(Base):
    __tablename__ = "learner"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user_L = relationship("User", back_populates="admin") #2
    
class Expert(Base):
    __tablename__ = "expert"

    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learner.id"))
    
    leaner = relationship("Learner", back_populates="expert")

class Syllabus(Base):
    __tablename__ = "syllabus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    lesson= relationship("Lesson", back_populates="syllabus")
    
class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    syllabus_id = Column(Integer, ForeignKey("syllabus.id"))
    
    syllabus = relationship("Syllabus", back_populates="lesson")
    
class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String(50), index=True)
    title = Column(String(50), index=True)
    viewCount = Column(Integer, index=True)
    description = Column(String(150), index=True)
    publishedAt = Column(String(50), index=True)
    thumbnails = Column(String(50), index=True)
    channel_id = Column(String(50), index=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    
    lesson = relationship("Lesson", back_populates="video")
    
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    videoid = Column(String, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


