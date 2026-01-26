
def Min_max(arr):

    '''Minimum = min(arr)
    Maximum = max(arr)
    return Minimum, Maximum

arr=[10,30,60,70,50,40,100,240,90]
print(Min_max(arr))'''


    if len(arr) == 0:
        return None,None
    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num <minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum,maximum 
arr=[101,30,60,70,50,40,100,240,90,1001] 
print(Min_max(arr))
      
