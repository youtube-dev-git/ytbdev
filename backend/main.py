
from typing import List
from winreg import QueryReflectionKey
from fastapi import FastAPI, HTTPException, status

from Permanent_Classes.syllabus import Syllabus
from Permanent_Classes.users import Admin, Learner, Expert
from DAO.DAOObjects import DAOObject
from Types import TypeUser, TypeSyllabus, TypeLogin
from videos_fetcher.system import System

app = FastAPI()

@app.post("/register", status_code = status.HTTP_201_CREATED)
def index(query : TypeUser):
    user = None
    # return Admin(
    #     name="jfdk",
    #     email="jfdk",
    #     phone_num="jfdk",
    #     password="jfdk",
    #     gender="jfdk",
    # )
    return query.user
    if(query.status == "admin"):
        user = Admin(**vars(query.user))
    elif(query.status == "learner"):
        user = Learner(**vars(query.user))
    elif(query.status == "expert"):
        user = Expert(**vars(query.user))
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail= "Invalid status")
        
    new_user = user.register()
    if not new_user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail= "The user already exists in the site")
    return new_user

@app.post("/login", status_code=status.HTTP_200_OK)
def index(request: TypeLogin):
    user = DAOObject.connect_user(request.email, request.password)
    # return {
        
    # }
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= "User not found")
    return user

@app.get("/login", status_code=status.HTTP_200_OK)
def index():
    return {
        "data" : "get worked"
    }

@app.post("/syllabus")
def saveTraining(query : TypeSyllabus):
    System.save_syllabus(query.expert_id, query.syllabus)
    return {
        "response" : "Insertion success"
    }

@app.get("/syllabus")
def listTrainings() -> List[Syllabus]:
    return DAOObject.list_trainings()

@app.get("/syllabus/{id}")
def listTrainings(expert_id : int) -> List[Syllabus]:
    return DAOObject.list_expert_trainings(expert_id)