
def Compare_string(str1 ,str2):
    if str1 != str2:
        print("Strings are Not Equals")
    elif str1 > str2:
        print("str1 is greater than str2")
    elif str1 < str2:
        print("str1 is less than str2")

    else:
        print("Strings are equals")

Compare_string("Hello","Hello")
Compare_string("Hello","HelloHello")
Compare_string("Hello Ganesh","Hello")
Compare_string("Hell","Hello")
