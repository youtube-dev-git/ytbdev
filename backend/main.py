
from typing import List
# from winreg import QueryReflectionKey
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from Permanent_Classes.syllabus import Syllabus
from Permanent_Classes.users import Admin, Learner, Expert
from DAO.DAOObjects import MainDAO
from Types import TypeUser, TypeSyllabus, TypeLogin
from videos_fetcher.system import System


@app.get("/")
def index():
    return { "data" : "Hello World"}

@app.post("/register", status_code = status.HTTP_201_CREATED)
def index(query : TypeUser):
    user = None
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
    user = MainDAO.connect_user(request.email, request.password)
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
    System.save_and_build_syllabus(query.expert_id, query.syllabus)
    return {
        "response" : "Insertion success"
    }

@app.get("/syllabus")
def listTrainings() -> List[Syllabus]:
    return MainDAO.list_trainings()

@app.get("/syllabus/{id}")
def listTrainings(expert_id : int) -> List[Syllabus]:
    return MainDAO.list_expert_trainings(expert_id)