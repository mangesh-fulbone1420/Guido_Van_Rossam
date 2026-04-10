n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("The Value of Factorial is ",fact)

# Take An input 
n=int(input("Enter the Number :"))
factorial=1
for i in range(1,n+1):
    factorial *=i
print("Your Factorial Value :",factorial)    

# Using Recursion Function
def fact(n):
    return 1 if n == 0 or n == 1 else n * fact(n - 1)

# Driver Code
n = int(input("Enter the number for recursive factorial: "))
print("The Factorial of Value is :", fact(n))