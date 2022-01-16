from fastapi import FastAPI
from .users import User
from ..DAO.DAOObjects import DAOObject

app = FastAPI()
db = DAOObject()

@app.post("/register")
def index(status: str, user : User):
    db.save_expert(user)
    pass