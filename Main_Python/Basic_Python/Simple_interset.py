def simple(p,t,r):
    si1=(p*t*r)/100
    return si1
    
p,t,r=10000,2,7    
si1 = simple(p,t,r)
print("The Simple interest is :",si1)

# Using Lambda Function

# Using Lambda Function

simple_interest = lambda p, t, r: (p * t * r) / 100
p, t, r = 10000, 2, 7
si = simple_interest(p, t, r)
print("The Simple Interest is :", si)

#Using the List Comprehension
p,t,r=10000,3,7
si=[(p*t*r)/100]
print("The Simple Interest is :",si)