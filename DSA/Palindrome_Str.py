
def palindrome(s):
    rev=""
    for i in s:
        rev=i+rev
    if s==rev:
        return True
    else:
        return False
print(palindrome("madam"))   
