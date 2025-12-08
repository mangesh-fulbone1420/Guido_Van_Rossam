
dict={'Roll_no':11,'Name':"Ganesh",'Marks':85,'Class':12,'Grade':"A+"}

print("Original Dictionary :",dict)

#Accessing Element in Dictionary 
print("Accessing Element in Dictionary :",dict['Name'])



print("Accessing Element in Dictionary using get() Method :",dict.get('Marks'))
# Delete Element in Dictionary
del dict['Grade']
print("After Deleting Element in Dictionary :",dict)

print("Length of Dictionary :",len(dict))

#adding Element in Dictionary
dict['Section']='A'
print("After Adding Element in Dictionary :",dict)