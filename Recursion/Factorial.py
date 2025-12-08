def fact(num):
    if num == 0 or num == 1 :
        return 1
    else:
        return num * fact(num-1)
    
num =int(input("Enter The Number :"))
result = fact (num)
print("The Factorial ",num ,"is :",result)

# 5*4*3*2*1=120
# Using The Above Code 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("Enter The Number :"))
res= factorial(n)
print("The Factorial of ", n ,"is :",res)

    
    