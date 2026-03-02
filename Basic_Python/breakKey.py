#find the smallest factor of a number
num=int(input("Enter The Number :"))

for i in range(2,num+1):
    if num % i == 0:
        print(i)
        break

    
