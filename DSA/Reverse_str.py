def reverse_str(s):
    return s[::-1]
s="Ganesh"
res=reverse_str(s)
print(res)

# Take Another Way 

def rev_str(str):
    rev=" "
    for i in str:
        rev=i+rev
    return rev
str="Ganesh"
result=rev_str(str)
print(result)