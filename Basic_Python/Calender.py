import calendar

year = int(input("Enter The Year :"))
month = int(input("Enter The Month :"))
#date = int(input("Enter The Date :"))
cal = calendar.month(year, month)

print(cal)

#yr = calendar.isleap(year)
#print(yr)