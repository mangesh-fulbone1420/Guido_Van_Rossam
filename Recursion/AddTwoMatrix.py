A=[[4,5,7],
   [8,5,9],
   [6,9,8]]

B=[[5,8,6],
   [9,4,3],
   [8,4,4]]

result =[[0,0,0],
         [0,0,0],
         [0,0,0]]

# using Nested Loop to Add Two Matrix
for i in range(len(A)):
    for j in range(len(A[0])):
       result[i][j]= A[i][j] + B[i][j]
#print in a Single Row        
print(result) 

# In A Matrix Form 
for r in result:
    print(r)       


#Using Recursion to add Two Matrix
'''def addMatrix(M,N,result, i,j):
    if i >=len(M):
        return 0
    if j >= len(M[0]):
        return addMatrix(M,N,result,i+1,0)
    result[i][j] = M[i][j] + N[i][j]
    addMatrix(M,N,result,i,j+1)
    addMatrix(M,N,result,0,0) 
M=[[4,5,7],
   [8,6,7],
   [9,7,5,]]  

N=[[6,3,9,],
   [9,2,7,],
   [6,3,7]]  

res=[[0,0,0],
     [0,0,0],
     [0,0,0]]  

addMatrix(M,N,res,0,0) 
for  re in res :
    print(re) '''
