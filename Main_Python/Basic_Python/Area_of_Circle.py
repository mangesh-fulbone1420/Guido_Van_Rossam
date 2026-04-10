import math as swami

rad =int(input("Enter the Radious of Circle :"))
area =swami.pi * (rad ** 2)
print("Thje Area of Circle is :", area)

 # using Function
def area_of_circle(r):
 return swami.pi * (r**2)
r=9
print("The Area of Circle is :",area_of_circle(r))