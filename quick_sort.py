import numpy as np
l1 = list(map(int, input().split()))
a = np.array(l1)
def r_to_l(a,loc,right):
    for i in range(loc,right):
        if a[loc] <= a[right] and loc !=right:
            right=right-1

        if a[loc]>a[right]:
            a[loc],a[right] = a[right],a[loc]
            loc=right
        if loc==right:
            # return loc,right
            break
    return a,loc

# a=[4,32,8,1,5,2]
t=r_to_l(a,0,len(a))