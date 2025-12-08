
def isogram(s):
    res={}
    for i in s:
        if i in res:
            return 0
        else:
            res[i]=1
    return 1
s="Ganesh"
ans=isogram(s)
print(ans)
        