
def reverse_String(str):

    rev=" "
    for i in str:
        rev = i + rev
    return rev

str = "Hello World"
print("Original String is : ", str)
print("Reverse String is : ", reverse_String(str)) 
   