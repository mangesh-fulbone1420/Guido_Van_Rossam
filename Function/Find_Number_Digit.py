
def Find_first_digit(num):
    while num >= 10:
        num=num//10
    return num

first=Find_first_digit(75757)  

print(first)


def Find_last_digit(num):
    return num%10
last=Find_last_digit(757574)
print(last)