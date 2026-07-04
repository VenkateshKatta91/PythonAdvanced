from pydantic import BaseModel, ValidationError, Field,field_validator,model_validator
from typing import Optional,Dict,List,Union,Any,Literal

class API_auth(BaseModel):  

    username:str=Field(...,min_length=3,max_length=20, description="This is the username")
    password:str=Field(...,min_length=8,max_length=20, description="This is the password")
    confirm_password:str=Field(...,min_length=8,max_length=20, description="This is the confirm password")
    email:str=Field(..., description="This is the email")

    @model_validator(mode='after')
    def password_check(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password and confirm password do not match")
        return values
pyd_ins=API_auth(**{"username":"John Snow","password":"password123","confirm_password":"password123","email":"johnsnow@gmail.com"})
print(pyd_ins)
print("Username:",pyd_ins.username)