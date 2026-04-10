num=eval(input("Enter The Number :"))
temp=num
sum=0
while temp > 0:
    rem=temp %10
    sum=sum*10 + rem
    temp=temp//10

if num==sum:
    print("The Given Number is Palindrome Number :",num)  
else:
    print("The Given Number is Not Palindrome Number :",num)  
