from pydantic import BaseModel, ValidationError, Field,computed_field
from typing import Optional,Dict,List,Union,Any,Literal

class input(BaseModel):

    query:str=Field(..., description="This is the query")
    
class output(BaseModel):

    query:str=Field(..., description="This is the query")
    result:str=Field(..., description="This is the result")

def process_data(p_input:input)->output:
    # Process the input data and generate output
    result=f"Processed query: {p_input.query}"
    return output(query=p_input.query, result=result)
    