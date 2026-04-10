
def Palindrome_arr(arr):
    arr1=arr
    i=0
    j=len(arr1)-1
    while i < j:
        arr1[i],arr1[j]=arr1[j],arr1[i]
        i+=1
        j-+1
        if arr==arr1:
            return True
        else:
            return False
print(Palindrome_arr([10,20,30,40,50,40,30,20,10]))
        