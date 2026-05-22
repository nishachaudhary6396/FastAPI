from pydantic import BaseModel, EmailStr, AnyUrl,Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):   # BaseModel is used to create models with type validation

    name: str = Annotated[str, Field(max_length=50, title="Name of the patient", example=['Nisha','Meet'])]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    url: AnyUrl
    weight:float = Annotated[float,Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the pateint married or not")]  # = False ..we can also set default values
    allergies: Optional[List[str]] = None # to make it optional
    contact_details: Dict[str,str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

patient_info = {'name': 'nisha', 'age': 22, 'email':'abc@gmail.com', 'url': 'https://hopitalmanagement.com','weight':47.3, 'married': True, 'contact_details': {'email':'abc@gmail.com', 'phone': '91190339333'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)