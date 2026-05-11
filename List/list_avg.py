
li=[10,20,30,40,50,60,70,80,90,100]
def list_avg():
    sum=0
    for i in li:
        sum +=i
        avg=sum/len(li)
    print("The Average of the list is :",avg)   
list_avg()

# Another way 
def list_avg1():
    avg1=sum(li) / len(li)
    print("The Average of the list using sum() function is :",avg1)
list_avg1()
    