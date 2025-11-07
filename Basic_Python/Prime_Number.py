import sympy as sp
s1 = sp.isprime(11)
s2= sp.isprime(21)
s3= sp.isprime(13)

print(s1)
print(s2)
print(s3)

#using math module
import math as mt
def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(mt.sqrt(n)) +1):
        if n % i == 0:
            return False
        return True
n=20
print("The Enter Given Number is Prime Number or Not : ",is_prime(n))  

# Take Loop

num =int(input("Enter The Number :"))
if num ==1:
    print("1 is neither prime nor composite")
for i in range(2,num):
    if num % i ==0:
        print(num,"is Not a Prime Number .")
        break
else:
    print(num,"is a Prime Number .")
