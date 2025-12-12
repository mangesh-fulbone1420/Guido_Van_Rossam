def palindrome_num(n):
    rev=0
    temp=n
    while temp >0:
        digit=temp%10
        rev=rev*10 +digit
        temp=temp//10
    if n == rev:
        return True
    else:
        return False

print(palindrome_num(141))

