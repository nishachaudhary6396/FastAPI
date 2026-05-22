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

temp = patient1.model_dump(include=['name','gender'])  # will give in dictionary
temp1 = patient1.model_dump_json() #will give as a string
print(temp)
print(type(temp)) 
print(temp1)
print(type(temp1))

# similary there is exclude method to not include

#exclude_unset=True    # at the tym of ctreating object the things which are not set at that tym that will not be export