#Perform other matrix operations like converting matrix data to absolute values, taking the
#negative of matrix values, additing/removing rows/columns from a matrix, finding the maximum
#or minimum values in a matrix or in a row/column, and finding the sum of some/all
#elements in a matrix

import numpy as np

B =np.array([-2,8.8,-12,90,-3.8,7.2,-80])
C= np.array([[7,8, 8],[3,7,9], [1,9, 10]])

absvalues=np.abs(B)

print("****Original values of B are****\n",B)
print("****Absolute values of B are****\n",absvalues)

negval=np.negative(B)
print("****Negative values of B are****\n",negval)

Bmax=np.max(B)
Bmin=np.amin(B)
print("****Maximum value of B is****\n",Bmax)
print("****Minimum values of B is****\n",Bmin)
print("\n****Matrix C is:***\n",C)
row=np.max(C[2,:])
print("****Maximum value of C's 2nd row is****\n",row)
col=np.amin(C[:,0])
print("****Minimum values of C's 0th column is****\n",col)

print("****Sum of all matrix elements of B is****\n",np.sum(B))
print("****Sum of all matrix elements of C is****\n",np.sum(C))
