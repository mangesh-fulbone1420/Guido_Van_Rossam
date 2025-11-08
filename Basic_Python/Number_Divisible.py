num=eval(input('Enter The Number :'))
print("The Divisible Number are :")

for i in range(1,num +1):
    if i %  14 ==0:
        print(i)


 # using lambda function and filter fun
# lambda function is an anonymous function
 #Create List of number 
l=[39,56,14,78,90,28,45,67,84,12,11,10]   

result = list(filter(lambda x : x% 14 == 0, l)) 
print("The Divisible Number using Lambda Function are :",result)   
