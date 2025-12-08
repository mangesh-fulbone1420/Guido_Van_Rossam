
str=input("Enter A String :")

print("Given String is :",str)
rev_str= str[::-1]

if str == rev_str:
    print("String is Palindrome.")
else:
    print("String is Not Palindrome.")

    # Using Function 
def is_palindrome(s):
    rev=s[::-1]
    if s== rev :
        return True
    else:
        return False  
s=input("Enter The String :")
if is_palindrome(s):
    print("String is Palindrome")
else:
    print("STring is Not Palindrome")


# Using Recursion
def is_palindrome_recursive(str1) :
    if len(str1) <= 1  :
        return True
    if str1[0] != str1[-1]:
        return False
    return is_palindrome_recursive(str1[1 : -1])
str1=input("Enter The  STring :")
if is_palindrome_recursive(str1):
    print("Your Entered String is Palindrome .")
else:
    print("Your Entered String is Not Palindrome .")


    


