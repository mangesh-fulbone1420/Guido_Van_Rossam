
def string_rev(str):

    rev=" "
    for i in str:
        rev = i+rev
    return rev

str=input("Enter a String :") 
print("Reverseof the String is :", string_rev(str))   

# Another way to reverse a string is by using slicing method

s="programming"
print(s[::-1])