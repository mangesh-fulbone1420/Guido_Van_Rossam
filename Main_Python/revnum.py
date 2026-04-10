num = 1234567
rev = 0
temp = num
while temp > 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp // 10

print("Original Number :", num)
print("Reverse Number :", rev)