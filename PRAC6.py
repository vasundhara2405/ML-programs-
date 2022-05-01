import numpy as np
A = np.array([[3,2,9],[1,5,6],[5,2,9]])
B = np.array([[7,8, 8],[3,7,9], [1,9, 10]])

print("****Matrix A is:\n",A,"\n****\n")
print("****Matrix B is:\n",B,"\n****\n")
print ("****The element wise addition of matrix is :\n ")
print (np.add(A,B))

print ("****The element wise subtraction of matrix is :\n")
print (np.subtract(A,B))

print ("****The element wise multiplication of matrix is :\n ")
print (A.dot(B))

print("****Specific rows or columns of A *****\n")
print("2nd row:",A[2],"\n")
print("1nd column:",A[:,1],"\n")

print("****Specific rows or columns of B *****\n")
print("2nd row:",B[2],"\n")
print("0nd column:",B[:,0],"\n")




