dict1={"Ganesh":95 , "Ramesh":89, "Krushna": 99}
dict2={"Suresh": 92 , "Mahesh": 87, "Ramesh": 96}

print("First Dictionary :",dict1 ,dict2)
# Merge Two Dictionarys
print( dict1 | dict2)

# Using the Exponentional operator  to merge two dictionarys

dict({**dict1 , **dict2})
print("Merged dictionary using Exponential Operator :", dict({**dict1, **dict2}))