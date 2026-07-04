from turtle import title
from urllib import response


class company:

    title:str="consultancy"

    def __init__(self,company_name:str):
        self.company_name:str=company_name

    def info(self):
        print(f"Company Name:{self.company_name}")
        return(f"Company Name:{self.company_name}")
# comp_obj=company("Tech Solutions")
# comp_obj.info()

class employee(company):

    def __init__(self, employee_name,company_name):

        self.employee_name=employee_name
        self.company_name=company_name
    
    def employee_info(self):
        response=company.info(self)
        print(f"The employee : {self.employee_name},{response}")
        
obj=employee("John","Tech Solutions")
obj.employee_info()