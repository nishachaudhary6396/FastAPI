from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):   # BaseModel is used to create models with type validation

    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
        


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

patient_info = {'name': 'nisha', 'age': 76, 'email':'abc@hdfc.com','weight':47.3, 'married': True, 'contact_details': { 'phone': '91190339333'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)