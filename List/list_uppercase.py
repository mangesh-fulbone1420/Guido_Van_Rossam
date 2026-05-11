
str=["hello", "world", "python", "programming", "list", "comprehension","python","geeksforgeeks"]

string=[s.upper() for s in str if s.startswith('p')]

print("The Uppercase String is :", string)

