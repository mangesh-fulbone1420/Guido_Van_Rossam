
# Using Continue and break keyword in a loop
li=[5,12,10,15,16,17,18,19,20]
for i  in li:
    if i % 5 == 0:
        break
    if i % 7 == 0:
        continue
    print(i)
print("Bye")    