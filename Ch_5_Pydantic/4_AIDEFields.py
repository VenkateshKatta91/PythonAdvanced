from operator import gt
from turtle import lt

from pydantic import BaseModel, Field,EmailStr 
from typing import Optional,Dict,List,Union,Any,Literal

class personal_info(BaseModel):

    name:str=Field(...,min_length=3,max_length=20, description="This is the name")
    age:Optional[int] =Field(...,ge=0, description="This is the age")
    email:EmailStr=Field(..., description="This is the email")
    gender:Literal["male","female","other"]=Field(..., description="This is the gender")
    salary:List[int]=Field(..., description="This is the salary")

def main(para1:personal_info):
    print("name:",para1.name)
    print("Age:",para1.age)
    print("Email:",para1.email)
    print("Gender:",para1.gender)
    print("Salary:",para1.salary)

pyd_ins=personal_info(**{"name":"John Snow","age":30,"email":"john@example.com","gender":"male","salary":[50000,60000]})
main(pyd_ins)