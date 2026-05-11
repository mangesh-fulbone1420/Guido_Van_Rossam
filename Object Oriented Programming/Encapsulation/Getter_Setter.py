# Getter :- Read Data using the Getter Method
# Setter :-Write Data using the setter Method.

class Employee:
    def __init__(self):
        self.__salary=100000 # private

    def get_salary(self): # getter method
        return self.__salary


    def set_salary(self,amount): # setter salary method
        if amount > 0:
            self.__salary=amount
        else:
            print("Invalid Salary Amount")

emp=Employee()
print(emp.get_salary()) # Accessing salary using getter method.

emp.set_salary(-150000) # Updating salary using setter method.
print(emp.get_salary()) # Accessing updated salary using getter method.


