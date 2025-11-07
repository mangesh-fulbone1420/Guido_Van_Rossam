
num=[1,3,2,1,2,3,1,0,1,3,]
current = None
for p in num:
    #print("The list is :",num)  
    if(p==0):
        current=p
        break
    elif(p%2==0):
        continue
    print(p)
print("The last even Number is :",current)