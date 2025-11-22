
a=[25,34,41,52,61,70,25,16,7]

print("Original List :", a)
a.sort()
print("Sorted List :", a)
a.append(10)
print("List After Appending 10 :", a)
a.remove(7)
print("List After Removing :",a)
a.reverse()
print("Reversed List :",a)
print("Length of the List is :", len(a))
print("Sum of the List :", sum(a))