#Using the continue keyword to skip current iteration of a loop
#num=int(input("Enter a Number :"))

li=[5,12,10,15,16,17,18,19,20]
for i in li:
    if i % 5 == 0:
        continue
    print(i)

