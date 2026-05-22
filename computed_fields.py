from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):   # BaseModel is used to create models with type validation

    name: str
    age: int
    email: EmailStr
    weight: float
    height: float
    married: bool
    contact_details: Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = self.weight/(self.height**2)
        return bmi
        

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.calculate_bmi)
    print(patient.contact_details)
    print('inserted')

patient_info = {'name': 'nisha', 'age': 76, 'email':'abc@hdfc.com','weight':47.3,'height': 2.71, 'married': True, 'contact_details': { 'phone': '91190339333','emergency': '94784785444'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)