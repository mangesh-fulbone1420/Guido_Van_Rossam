# Array is an acontiguous memory location that stores multiple values of the same type.
#String is a Sequence of Characters.
# Stack is a Linear Data Structure That Follows a a particular order in which the operations are performed.
#The Stack Follows the LIFO (Last In First Out ) Principle.
#The Queue is a Linear Data Structure That Follows a  FIFO (First In First Out) Principle.
# Type of Queue are Simple Queue,Circular Queue,priority Queue and Deque.
#Linked list  is Linear Data Structure in which the Elements are not Stored in Contiguous Memory Locations.
# Type of linked List are Singly Linked List ,Doubly Linked list and circular linked list.
#A linked List is a Sequence of Data Structures, Which are connected together via Links.
#A Tree is a Non-Linear Data Structure that orgnizes data in a hierarchical manner .
#
#A Graphb is aNon-Linear Data structure that consists of a finite set of vertices (or nodes) and a set of edges connecting that vertices.
#The Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems.
#DP is applicable for optimization problems wher the problems can be divided into overlapping sub-problems which can be solveed independently .
#Recursion is a programming technique in which a function calls itself deirectly or indirectly to solve a problem.



# sum of the nth natural number r
num = int (input ("Enter The Natural Number :")) 

sum= num*(num+1) //2
print("The Sum of the first",num,"natural Number is : ", sum)

# Sum of n th natural number using  for loop
num1= int (input ("Enter The Natural Number :"))
sum1=0
for i in range (1,num1 + 1):
    sum1 = sum1 +i
print("The sum of the first ",num1 ,"natural Number is : ",sum1)


# Sum of n th natural number using while loop
num2 = int(input("Enter The natural Number  :"))
sum2=0
i=1
while i <= num2:
    sum2 = sum2 + i
    i += 1
print("The sum of the first ", num2 ," natural Number is : ", sum2 )  

# Sum of the nth natural number using Recursion
def natural_sum(n):
    if n==1:
        return 1
    else:
        return n + natural_sum(n-1)
num3 = int(input("Enter The Natural Number : "))
result = natural_sum(num3)  
print("The sum of the first ", num3 ," natural Number is : ", result)  

#Using 



# Sum of n th natural number using Dynamic Programming
num4 = int(input("Enter The Natural Number : "))
dp = [0] * (num4 + 1)
dp[1] = 1   
for i in range(2, num4 + 1):
    dp[i] = dp[i - 1] + i       
print("The sum of the first ", num4 ," natural Number is : ", dp[num4])
