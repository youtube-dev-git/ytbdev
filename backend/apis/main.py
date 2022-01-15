
from fastapi import FastAPI, status

from pydantic import BaseModel

from typing import List, Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///ydev.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create the database
Base.metadata.create_all(engine)

app = FastAPI()

class Inscription(BaseModel):
    name : str
    email: str
    passord: str
    genre: str
    statut: str
    photo: Optional[str]
    tel: int
class Admin(BaseModel):
    id_Admin:int
    name : str
    email: str
    passord: str
    genre: str
    photo: Optional[str]
    tel: int
    id_Learner:int
    id_Expert:int
class leaner(BaseModel):
    id_Learner:int
    name : str
    email: str
    passord: str
    genre: str
    photo: Optional[str]
    tel: int
    id_Admin:int
    id_Expert:int

class Expert(BaseModel):
    id_Expert:int
    name : str
    email: str
    passord: str
    genre: str
    photo: Optional[str]
    tel: int
    id_Admin:int
    id_Learner:int

@app.get("/")
def root():
    return "subscription"

@app.post("/subscription ", status_code=status.HTTP_201_CREATED)
def create_subscription(inscription: Inscription ):
    return "create subscription "

@app.get("/subscription/{id}")
def read_subscription(id: int):
    return "read subscription  with id {id}"

@app.put("/subscription/{id}")
def update_subscription(id: int):
    return "update subscription  with id {id}"

@app.delete("/subscription/{id}")
def delete_subscription(id: int):
    return "delete subscription  with id {id}"

@app.get("/subscription")
def read_subscription_list():
    return "read subscription list"