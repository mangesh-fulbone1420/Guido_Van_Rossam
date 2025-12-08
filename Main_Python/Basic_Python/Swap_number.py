a=10
b=20
print("Before Swapping : a=",a ,"b=",b)
temp=a
a=b
b=temp
print("After Swapping :a=",a ,"b=",b)


# Without using Third variable
x=15
y=25
print("Before Swapping : x=",x ,"y=",y)
x,y=y,x
print("After Swapping : x=",x ,"y=",y)

# Using Airthmatic Operation
m= 20
n=30
print("Before Swapping : m=",m ,"n=",n)
m=m+n
n=m-n
m=m-n
print("After Swapping : m=",m ,"n=",n)
