# To print Even Number 1-20 Without Loop
num = int(input("Enter The Number: "))
if num % 2 == 0:
    print("The Given Number is Even Number.")
else:
    print("The Given Number is Odd Number.")

# without Loop
def print_even(n):
    if n > 20:
        return
    print(n)
    print_even(n + 2)

print_even(2)

    