import time
def Replace_Zero(n):
    str_n = str(n)
    res = " "
    for i in str_n:
        if i == '0':
            res += '5'
            time.sleep(5)
        else:
            res += i
    return int(res)

print("Replace Zero with Five in Given Number : ", Replace_Zero(102030))