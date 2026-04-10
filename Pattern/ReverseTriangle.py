n=int(input("Enter The Number of Rows:"))

# Reverse Trianfle Pattern using nested Loop
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
        