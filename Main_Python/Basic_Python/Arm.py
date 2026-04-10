num=eval(input("Enter The Number :"))

temp=num
sum=0
while temp > 0:
    rem =temp % 10
    sum = sum + rem ** 3
    temp = temp // 10
if sum == num:
    print("The Enter Number is Armstrong Number :",num)
else:
    print("The Enter Number is Not Armstrong Number :",num)
