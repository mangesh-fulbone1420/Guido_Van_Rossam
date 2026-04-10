year=int(input("Enter The Year :"))

if (year % 4== 0 and year % 100 != 0) or (year % 400 ==0):
    print("{0} is a Leap Year". format(year))
else:
    print("{0} is Not a Leap Year". format(year))       