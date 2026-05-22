#Benefits->
# 1. Better Organization of related data
# 2. Reusability
# 3. Readablity
# 4. Validation


from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dictionary = {'city':'Agra','state':'UP','pin':'282007'}

addresss = Address(**address_dictionary)

patient_dict = {'name':'nisha','gender':'female','age':22, 'address': addresss}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)