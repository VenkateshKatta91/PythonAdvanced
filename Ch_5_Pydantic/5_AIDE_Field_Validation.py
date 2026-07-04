from pydantic import BaseModel, ValidationError, field_validator,Field 
from typing import Optional,Dict,List,Union,Any,Literal

class personal_info(BaseModel):

    name:str=Field(...,min_length=3,max_length=20, description="This is the name")
    age:Optional[int] =Field(...,ge=0, description="This is the age")
    email:str=Field(..., description="This is the email")

    #Field validator for email
    @field_validator('email')
    def email_check(cls, value):
        if "@" not in value or ".com" not in value:
            raise ValueError("Invalid email address")
        return value
    
pyd_ins=personal_info(**{"name":"John Snow","age":30,"email":"john@example.com"})

print(pyd_ins)