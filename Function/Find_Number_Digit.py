
def Find_first_digit(num):
    while num>=10:
        num=num//10
    return num  
first_digit=Find_first_digit(7909876787) 
print(first_digit) 

def Find_last_digit(num):
    return num%10
last=Find_last_digit(757574)
print(last)