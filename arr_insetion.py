#  insertion of element in array
l1 = [5,4,6,7,2]
temp = []
s=[]
l2 = []
pos = int(input("enter position : "))
num = int(input("enter a number : "))
pos=pos-2

for i in range(0,len(l1)):
    temp = l1[i]
    if pos>i:
        l2 = l2+[temp]
    elif pos == i:
        l2=l2+[temp]
        l2 = l2+[num]
    else:
        l2=l2+[temp]
            # l1[pos]=num

    # l1=l1+[temp]

print(l2)