
num=12345
num_str=str(num)
print("Original Number :",num)
print("Reverse Number :",num_str[::-1])
print("Length of the Number : ",len(num_str))
for i in range(len(num_str)-1,-1,-1):
    print(num_str[i],end="")


