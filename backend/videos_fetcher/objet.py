from fastapi import FastAPI

from system import System
from primarySyllabus import PrimarySyllabus

app = FastAPI()

    
@app.post('/objet')
def create(request : PrimarySyllabus):
    syllabus = request.syllabusConversion()
    System.save_syllabus(request)
    return request
    