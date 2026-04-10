a=75
b=85 
sum=a+b
print("Sum of A and B is :",sum)

#Give an User Input
a=eval(input("Enter the valueof A : "))
b=eval(input("Enter The Value of B :"))

sum = a + b
print("sum of A and B is : ",sum)

#using Function

def add (a,b):
    return a+b

a=75
b=85

sum= add (a,b)
print("Sum of the a and B is :", sum)

#Lambda Function
add =lambda a , b : a + b
a=75
b=85
sum=(add(a,b))
print("Sum of A and B is :",sum)


#using operator module
import operator
a=75
b=85
sum=operator.add(a,b)
print("The Addition of A and B is :",sum )