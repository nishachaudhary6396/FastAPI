from pydantic import BaseModel

class Patient(BaseModel):   # BaseModel is used to create models with type validation

    name: str
    age: int


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)


patient_info = {'name': 'nisha', 'age': 22}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)