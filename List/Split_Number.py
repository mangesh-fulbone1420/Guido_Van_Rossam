#Extract Even and odd Number from list

li=[1,2,3,4,5,6,7,8,9,10]
def split_Number():
    evens=[n for n in li if n% 2==0]
    odds=[n for n in li  if n%2 !=0]
    print("Even Numbers are :",evens)
    print("odd Numbers are :",odds)
split_Number()