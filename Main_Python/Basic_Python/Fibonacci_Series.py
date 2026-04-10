count = int(input("Enter The Count of Fibonacci Series :"))
n1, n2 = 0, 1
print("Fibonacci Series is :", n1, " ", n2, end="")

for i in range(2,count):
    n3= n1+n2
    n1=n2
    n2=n3
    print(" ",n3,end="")