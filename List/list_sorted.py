def list_sorted(li):

    i=1
    while i<len(li):
        if li[i ] < li[i-1]:
            return False
        i+=1
    return True

li=[10,20,30,35,40,50]   

print(list_sorted(li)) 

# Another way to  using sorted () function

def sorted_list(l):
    rev=l.copy()
    rev.reverse()
    sl=sorted(rev)

    if sl==rev:
        return True
    else:
        return False

l=[50,40,30,20,10]  
print(sorted_list(l))
