from typing import List
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Objet(BaseModel):
    title : str
    lessons: List
    
@app.post('/objet')
def create( request : Objet):

    return request
    