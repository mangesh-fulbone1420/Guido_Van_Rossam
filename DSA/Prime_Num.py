def isprime(n):
    start = 2
    end=n//2 + 1
    for i in range(start ,end):
        if n % i == 0:
            return False
    return True
num =10
if isprime(num):
    print("The Number is Prime") 
else:
    print("The Number is Not Prime")   