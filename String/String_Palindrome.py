def String_Palindrome(str):

    if str== str[::-1]:
        print("String is Palindrome ")
    else:
        print("String is not Palindrome")

str=input("Enter A String to check String is Palindrome or Not :")
String_Palindrome(str)   
