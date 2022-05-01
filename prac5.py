#Use command to compute the size of a matrix, size/length of a particular row/column, load
#data from a text file, store matrix data to a text file, finding out variables and their features in the
#current scope



import numpy as np



A=np.array([10,20,40,60])

B =np.array([[7,8, 8],[3,7,9], [1,9, 10],[2,7,9]])
C= np.array([[7,8, 8],[3,7,9], [1,9, 10]])
print("****Matrix A is:***\n",A)
print("****SIZE of A is:***\n",A.ndim)
print("\n****Matrix B is:***\n",B)
print("****SIZE of B is:***\n",len(B),"X",len(B[0]))
print("\n****Matrix C is:***\n",C)
print("****SIZE of C is:***\n",len(C),"X",len(C[0]))

print("****Length of specific rows or columns of C *****\n")
print("1nd column:",len(C[:,1]),"\n")
print("0rd row:",len(C[0,:]),"\n")

print("****Length of specific rows or columns of B *****\n")
print("2nd row:",len(B[2,:]),"\n")
print("0rd column:",len(B[:,0]),"\n")


filee=open("C:/Users/shwet/Desktop/mera kaam/ML/Hello1.txt","r")
cont=filee.read()
print("***contents of Hello1.txt are:***\n",cont)

np.savetxt("matrixprint.txt",B)
contents=np.loadtxt("matrixprint.txt")
print("****contents of matrixprint.txt are:***\n",contents)

