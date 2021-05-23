l1=list(map(int,input("enter list items  :").split()))
ele = int(input("enter "))
l2=[]
for i in l1:
    if ele==i:
        temp=i
    else:
        l2=l2+[i]
print(l2)