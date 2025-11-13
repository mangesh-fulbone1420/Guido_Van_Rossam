#  Fibonacci Series Using Iteration
''' num=int(input("Enter The Count :"))

n1,n2 =0,1

print("Fibonacci Sequence :",n1,',',n2,end=" ")

for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(',',n3,end = "") '''


#Using Recursion
def fibonacci(n):
    if n <=1:
        return n
    else:
        return(fibonacci(n-1 )+fibonacci(n-2))
#fib=fibonacci(5)   
#print("Fibonacci Series is :",fib) 

num =int(input("Enter The Count :"))
if num <= 0:
    print("Please Enter Positive  Number :")
else:
    print("Fibonacci Series is :")
    for i in range(num):
        print(fibonacci(i), end=" ,")
              
