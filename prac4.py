#Create/Define single dimension / multi-dimension arrays, and arrays with specific values like
#array of all ones, all zeros, array with random values within a range, or a diagonal matrix.
#

import numpy as np



A=np.array([10,20,40,60])

B =np.array([[7,8, 8],[3,7,9], [1,9, 10],[2,7,9]])
C= np.array([[7,8, 8],[3,7,9], [1,9, 10]])
D=np.array([[7,8, 8], [1,0, 10]])
E=np.ones((3,2))
F=np.identity(3)
G=np.random.random((3,3))
H=np.zeros([4,4])
print("****Matrix A is:***\n",A)
print("\n****Matrix B is:***\n",B)
print("\n****Matrix C is:***\n",C)
print("\n****Matrix D is:***\n",D)
print("\n****Matrix E is:***\n",E)
print("\n****Matrix F is:***\n",F)
print("\n****Matrix G is:***\n",G)
print("\n****Matrix H is:***\n",H)