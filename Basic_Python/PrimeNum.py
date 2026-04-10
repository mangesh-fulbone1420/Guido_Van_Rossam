
# Take Input From The User
num=int(input("Enter The Number :"))

#Check the First Condition to number is prime or not
if num <= 1:
    print(num,"is not prime Number because it is less than or equal to 1")
else:
    #Chesk the Second Condition to Number is prime or Not
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not prime number because it is divisible by",i)
    else:
        print(num,"is a prime Number")