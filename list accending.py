l1=list(map(int,input().split()))
l2=[]
max=0
temp=0
for i in range(len(l1)):
    if l1[i] > max:
        max = l1[i]
        l2.append(max)
    else:
        for j in range(0,len(l2)):
            if l2[j] >l1[i]:
                l2.insert(j,l1[i])
                break









print(l2)



