from pydantic import BaseModel, ValidationError, Field,StrictInt

class input(BaseModel):

    x:StrictInt=Field(..., description="This is the x")
    y:str=Field(..., description="This is the y")

pyd_input=input(**{"x":10, "y":"hello"})
print(pyd_input)