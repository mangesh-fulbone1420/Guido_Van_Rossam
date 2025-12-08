
def natural(num):
    if num <= 1:
        return num
    else:
        return num + natural(num -1)
num =int(input("Enter The Natural Number :"))
result = natural(num)
print("The Sum of the Natural Number is :",result)