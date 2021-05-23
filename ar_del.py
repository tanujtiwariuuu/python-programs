l1 = [4,5,8,6,2,1,7,8,9,6]
temp = 0
l2 = []
s=0
pos = int(input(" enter position"))
for i in range(0,len(l1)):
    temp = l1[i]
    if pos == i:
        s=temp
    else:
        l2=l2+[temp]
print(l2)