class Student:
    def __init__ (self):
        self.name="Ganesh"
        self.College="Trinity Academy Of Engineering,Pune" 
        self.branch="MCA ENGG"
        self.designation="Azure Data Engineer"
        self.company="MasterCard India PVT LTD"
        self.package="14 LPA"
        self.location ="Pune,Maharashtra"
    def display(self):

        print("Name :",self.name)
        print("College :",self.College)
        print("Branch :",self.branch)
        print("Designation :",self.designation)
        print("Company :",self.company)
        print("Package :",self.package)
        print("Location :",self.location)

s1 = Student()
s1.display()
           
