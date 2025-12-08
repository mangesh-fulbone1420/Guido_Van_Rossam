
#num=int(input("Enter The Natural Number :"))
#sum = num*(num+1)/2
#print("The Sum of the first ",num,"natural Number is : ",sum)

num =int(input("Enter the Natural Number :"))

if num <= 0:
    print("Please Enter a Positive Number ")
else:
    sum=0
    while num > 0:
        sum += num
        num -=1
print("The Sum os the First Natural Number Sum :",sum)