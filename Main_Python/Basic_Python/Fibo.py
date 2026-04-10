num=eval(input("Enter The Number :"))

num1,num2=0,1

print("Fibonacci Series is :",num1,",",num2,end=" ")
for i in range (0,num):
   # print(num1)
    num3=num1+num2
    num1=num2
    num2=num3
    print(",",num3, end=" ")
