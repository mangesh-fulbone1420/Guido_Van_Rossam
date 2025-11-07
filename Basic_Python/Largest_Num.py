a=int(input("Enter the Number Of A :"))
b=int(input("Enter the Number Of B :"))
c=int(input("Enter the Number Of C :"))
if(a>=b>=c):
    large =a
elif(b>=a>=c):
    large =b
else:
    large =c
    print("The Largest Number is : ",large)