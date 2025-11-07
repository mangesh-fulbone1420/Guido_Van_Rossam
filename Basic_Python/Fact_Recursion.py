def fact(num):
    if num ==1:
        return 1
    
    return num * fact(num -1)

num= eval(input("Enter The Number :"))
result =fact(num)
print("The Factorial of Given Number is :",result)