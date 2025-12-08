a=7
b=5
print("The Max Value :",max(a,b))

# Take An User Input
a=eval(input("Enter The Number A :"))
b=eval(input("Enter The Number B :"))
c=eval(input("Enter The Number C :"))

print("The Maximum value :",max(a,b,c))
print("The Minimum value :",min(a,b,c))

#Using an ternary Operator
a=33
b=25
c=27
print(a if a > b else b )

#using the if and Else statement

#a=33
#b=25

if(a>b):
    print("Max Value A ",a)
if(b>c):
    print("Max Value B ",b)
if(c>a):
    print("Max Value C ",c)    
else:
    print ("Invalid")   



