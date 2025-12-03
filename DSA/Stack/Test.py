num=int(input("Enter The Natural Number :"))
arr=[1,2,3,4,5,6,7,8,9]

output=[ ]
for i in range(len(arr)):
    if i%2==0:
        output.append(arr[i])
        #print("To sort the Alternate Element in the List :",output)
    else:
        continue
print("To Sort the Alternate Element in the List :", output)     
#--- IGNORE ---
#print("Programming is Easy")
