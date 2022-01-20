
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50), unique=True, index=True)
    password = Column(String(50), unique=True, index=True)
    photo = Column(String(50), unique=True, index=True)
    gender = Column(String(10), unique=True, index=True)
    phone = Column(String(15), unique=True, index=True)
    #status = Column(Integer,index=True)
    
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True) 
    
    #admin = relationship("user", back_populates="admin")
   
class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50), unique=True, index=True)
    #password = Column(String(50), unique=True, index=True)
    photo = Column(String(50), unique=True, index=True)
    gender = Column(String(10), unique=True, index=True)
    phone = Column(String(15), unique=True, index=True)
    #status = Column(Integer,index=True)
    statut = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)
    #user = relationship("admin", back_populates="users")

class Expert(Base):
    __tablename__ = "expert"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50), unique=True, index=True)
    photo = Column(String(50), unique=True, index=True)
    gender = Column(String(10), unique=True, index=True)
    phone = Column(String(15), unique=True, index=True)
    statut = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)
    

class Learner(Base):
    __tablename__ = "Learner"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50), unique=True, index=True)
    photo = Column(String(50), unique=True, index=True)
    gender = Column(String(10), unique=True, index=True)
    phone = Column(String(15), unique=True, index=True)
    statut = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)