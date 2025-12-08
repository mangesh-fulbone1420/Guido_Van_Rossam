
print("------------Simploe Calculator------------")
num1=eval(input("Enter The Number 1 :"))
num2=eval(input("Enter The Number 2 :"))


print("Press 1 for Addition \n Press 2 For substraction \n Press 3 For Multiplication \n Press 4 For Division \n")
choice = int (input("Enter You Want Perform operation :"))
if choice ==1:
    print("The Addition of Given Number is :", num1 + num2)
elif choice == 2:
    print("The Substraction of Given Number is :", num1 - num2)
elif choice == 3:
    print("The Multiplication of the Given Number is :", num1 * num2 )
elif choice == 4:
    print("The Divion of Given Number is :",num1 / num2 )
else:
    print("Invalid Input")
    