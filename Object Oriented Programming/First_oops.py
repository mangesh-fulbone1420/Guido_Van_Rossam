# First OOPS program in python
# OOPS stands for Object Oriented Programming System. 
# It is a programming paradigm that uses objects and classes to design and implement software.
#  In OOPS, we can create objects that have properties (attributes) and behaviors (methods).
class dog:
    age=10
    # create a Constructor to initialize the properties of the class.
    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color

obj=dog("Tommy","German Shephard","Black") 
print(obj.name,obj.breed,obj.color)

print(obj.age)
