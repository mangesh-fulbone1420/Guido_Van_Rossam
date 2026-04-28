#  encapsulation is to bind the data members and methods into a single unit.
# used private Atributes and methods to achieve Encapsulation

class Emp:
    id=101
    def __init__(self,name,salary):
        self.name=name # public attribute
        self.__salary=salary # private attribute
    
employee=Emp("Ganesh",100000)
print(employee.name)  # Public attribute can be Accessed outside the class.
print(employee.__salary) # private Attribute cannot be accessed outside the class .It will give an error.

