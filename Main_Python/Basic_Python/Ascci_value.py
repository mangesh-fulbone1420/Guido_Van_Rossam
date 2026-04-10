
value = eval(input("Enter A Character :"))

print("The ASCII Value of ", value, "is :", ord(value)) 


print("Enter String :")
s= input()
textlength=len(s)
print("The Length of the String is :", textlength)
for i in s:
    print("The ASCII Value of ", i, "is :", ord(i))
    ascii = ord(i)

    print(i, "\t", ascii)