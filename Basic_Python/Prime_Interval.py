lr=int(input("Enter The Lower Limit:"))
ur=int(input("Enter The Upper Limit:"))
sum =0
for num in range (lr,ur+1):
    if  num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            sum+=num
print("The Sum of the Prime Number in Given interval is :", sum)            

