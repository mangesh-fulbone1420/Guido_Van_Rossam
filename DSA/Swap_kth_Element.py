
def swap(arr,k):
    n=arr[k]
    arr[k-1],arr[k-n]=arr[k-n],arr[k-1]
    return arr

arr=[10,20,30,40,50,60,70] 
k=7
print(swap(arr,k))