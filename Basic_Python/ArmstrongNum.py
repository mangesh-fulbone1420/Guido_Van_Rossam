n=int(input("Enter the Number :"))

temp=n
sum=0
while temp > 0:
   rem =temp % 10
   sum += rem ** 3
   temp = temp // 10
if sum == n:
     print("The Enter Given Number is Armstrong Number :",n)
else:
     print("The Enter Given Number is Not ArmStrong Number :",n)




# using String Manipulation
#num = int (input(":Enter The Number To check Number is ArmStrong or Not :"))
def armstrong(num):
    num_str = str(num)
    n1 = len(num_str)
    sum = 0
    for i in range(n1):
        sum += int(num_str[i]) ** n1
    if sum == num:
        return True
    else:
        return False
num =153
print("The Number is Armstrong Number :",armstrong(num))    
