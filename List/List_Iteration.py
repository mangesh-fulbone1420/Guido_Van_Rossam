li=[1,2,3,4,5,6,7]
rev=" "
for i in range(len(li)-1,-1,-1):
    rev=rev+str(li[i])
print("Reverse list is :",rev)    