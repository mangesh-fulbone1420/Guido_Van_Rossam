num=int(input("Enter The Star Value :"))

for i in range(num,0,-1):
    for j in range(i):
        print("*", end=" ")
    print( )    