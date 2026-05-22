from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json
from fastapi.responses import JSONResponse
app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str,Field(..., description='ID of the patient', examples=['POO2'])]
    name: Annotated[str,Field(..., description='Name of the Patient')]
    city: Annotated[str, Field(..., description='Patient City')]
    age: Annotated[int, Field(...,gt=0, lt=90, description='Age of the patient')]
    gender: Annotated[Literal['male','female','others'],Field(..., description='provide gender of the patient')]
    height: Annotated[float,Field(..., gt=0,description='Height of the patient')]
    weight: Annotated[float,Field(...,gt=0,description='Weight of the patient in kg')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 45:
            return 'Underweight'
        elif self.bmi< 55:
            return 'normal'
        elif self.bmi < 65:
            return 'normal'
        else:
            return 'Overweight'

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message": "Patient Management"}

@app.get('/view')
def view():
    data = load_data()
    return data


@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()   #load existing data

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient allready exist')  #check if the patient allready exists
    
    data[patient.id] = patient.model_dump(exclude=['id'])  #new patient add to the db

    #save
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'added successfully'})




    
