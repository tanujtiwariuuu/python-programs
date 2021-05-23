import numpy as np
arr = list(map(int,input("input space seprated sorted array elements : ").split()))
b=np.array(arr)
target = int(input('target : '))
lb= 0
ub = len(b)
while True:
    mid = (lb+ub)//2
    if b[mid] == target:
        print(f'found at location {mid+1}')
        break

    elif b[mid]>target:
        ub = mid
    elif b[mid]<target :
        lb = mid+1
