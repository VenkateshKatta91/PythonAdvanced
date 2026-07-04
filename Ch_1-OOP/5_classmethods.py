class Myclass:

    my_var=100

    @classmethod
    def change_value(cls,new_value):
        cls.my_var=new_value
    
#     def change_value(self,new_value):
#         Myclass.my_var=new_value

obj1=Myclass()
print(obj1.my_var)
obj1.change_value(200)
print(obj1.my_var)
obj2=Myclass()
print(obj2.my_var)    