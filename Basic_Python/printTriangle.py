
num=int(input("Enter The Numer :"))

for i in range(num):
    for  j in range(num-i):
        print("*" ,end=" ")
    print()    

#Useing another way to print triangle pattern
for i in range(num,0,-1):
    for  j in range(i   ):
        print("*" ,end=" ")
    print()        