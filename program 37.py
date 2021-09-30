'''program to transpose a matrix'''

import numpy as np
a=np.array([[1,2,3,4,5,6],[2,3,4,6,7,9]])

# transpose by using function
a=np.transpose(a)
print(a)

# transpose by using logic
print("transpose of the matrix is: ")
b=np.array([[1,2,3,4],[5,6,7,8]])
# creation of an empty matrix
c=np.empty((4,2),dtype='int')
for i in range(2):
    for j in range(4):
        c[j][i]=b[i][j]
print(c)