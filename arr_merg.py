l1 = [4,3,5,7,1]
temp=0
m= []
for i in range (0,len(l1)):
    temp = l1[i]
    if temp > l1:
        m = m+[temp]
    else:
        m= m+[l1[i]]
print(m)
