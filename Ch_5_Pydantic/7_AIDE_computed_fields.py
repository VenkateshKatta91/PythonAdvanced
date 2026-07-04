from pydantic import BaseModel, ValidationError, Field,field_validator,model_validator,computed_field
from typing import Optional,Dict,List,Union,Any,Literal

class orders(BaseModel):

    order_id:int=Field(..., description="This is the order id")
    product_name:str=Field(..., description="This is the product name")
    quantity:int=Field(..., description="This is the quantity")
    price:float=Field(..., description="This is the price")
    
    @computed_field
    def total_price(self)->float:
        return self.quantity * self.price
    
pyd_ins=orders(**{"order_id":1,"product_name":"Laptop","quantity":2,"price":500.0})
print(pyd_ins)
print("Total Price:", pyd_ins.total_price)