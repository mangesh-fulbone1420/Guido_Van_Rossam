li=[10,20,10,30,30,20,40,50]

res=1
for i in range(1,len(li)):
    if li[i] not in li[0:i]:
        res=res+1
print(res)        