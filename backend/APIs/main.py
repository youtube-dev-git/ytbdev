from typing import List
from fastapi import FastAPI, HTTPException, status

from ..Permanent_Classes.syllabus import Syllabus
from ..Permanent_Classes.users import TypeUser, Admin, Learner, Expert
from ..DAO.DAOObjects import DAOObject

app = FastAPI()
db = DAOObject()

@app.post("/register", status_code = status.HTTP_201_CREATED)
def index(query : TypeUser):
    user = None
    if(query.status == "admin"):
        user = Admin(**query.user)
    elif(query.status == "learner"):
        user = Learner(**query.user)
    elif(query.status == "expert"):
        user = Expert(**query.user)
    new_user = user.register()
    if not new_user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail= "The user already exists in the site")
    return new_user

@app.get("/login")
def index(email:str, password: str):
    user = db.connect_user(email, password)
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= "User not found")
        
    return user

@app.get("/syllabus")
def listTrainings(syllabusList : List[Syllabus]):
    return db.read_syllabus_videos()

@app.get("/syllabus/{id}")
def listTrainings(id, syllabusList : List[Syllabus]):
    return db.read_syllabus_videos()