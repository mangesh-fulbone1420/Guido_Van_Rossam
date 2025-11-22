
str="Python Is Popular Programming Language"
vowels="aeiouAEIOU"

str=str.casefold()

print("Original String :", str)

count={}.fromkeys(vowels,0)

for i in str:
    if i in count:
        count[i]+=1
print("Vowels in the Given String :",count)        