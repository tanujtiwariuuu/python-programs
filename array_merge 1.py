#  merge 2 array or list in accending order method 1 :
l3 = []
l1 = [7,4,6,2,8,1]
l2 = [5,6,1,8,3]
l3 = l1+l2
for i in range(0,len(l3)):
    if l3[i]:
        i = 0
        while i != len(l3) - 1:
            if l3[i] >= l3[i + 1]:
                temp = l3[i]
                l3[i] = l3[i + 1]
                l3[i + 1] = temp

            i = i + 1

print(l3)
