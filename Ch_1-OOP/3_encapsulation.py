class MyClass:

    #Class Variables
    var1="Venkatesh"
    var2="Katta"
    
    #Instance Variables
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1=dyn1 #Public Variable
        self.__dyn2=dyn2 #Private Variable
        self._dyn3=dyn3 #Protected Variable
    #Class Methods
    def func1(self):
        print(f"Hello World , {self.dyn1}")

    def func2(self):
        print(f"Hello Globe , {self.__dyn2}")

    def func3(self):
        print(f"Hello Globe , {self.dyn3}")

obj=MyClass("abc","def","xyz")
print(obj.dyn1)

print(obj._dyn3)