
li=[10,20,30,40,50,60,70,80,90,100]

def list_sum():
    sum=0
    for i in li :
        sum +=i
    print("The sum of the list is :",sum)
list_sum()


# Another method to add the list using the sum() function
def list_sum1():
    sum1=sum(li)
    print("The sum of the list using sum() function is :",sum1)
list_sum1()   



