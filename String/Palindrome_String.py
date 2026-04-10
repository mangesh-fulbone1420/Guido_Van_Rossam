# To Check String is Palindrome or Not using the slicing method

def palindrome_string(str):

    if str == str[::-1]:
        print("String is Palindrome")
    else:
        print("String is Not Palindrome")

str=input("Enter The String to check String is Palindrome or Not :")
palindrome_string(str)


#Using iteration method
def palindrome_string(s):

    rev = " "
    for i in s:
        rev = i + rev

    if s == rev:
        print("String is Palindrome")
    else:
        print("String is Not Palindrome")

s="madam"
palindrome_string(s)




