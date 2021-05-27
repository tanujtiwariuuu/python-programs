import numpy as np
l1 = []
print('elements of array 1 : ')
n =int(input('arr 1 rows : '))
for i in range(n):
    l1 = l1+[list(map(int, input().split()))]
arr1 = np.asarray(l1)
print('elements of array2 : ')
l1 = []
m=int(input('arr 2 rows : '))
for i in range(m):
    l1 = l1+[list(map(int, input().split()))]
arr2 = np.asarray(l1)
arr2 = arr2.T
l2 = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        l2.append(sum(arr1[i]*arr2[j]))
arr1 = np.asarray(l2).reshape(n, n)
print(arr1)