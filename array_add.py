l1 = []
l2=[]
l3 =[]
h=int(input("how many element in l1 and l2 : "))
for i in range(0,h):
    l1 = l1+[int(input("ele : l1 "))]
for k in range(h):
    l2 = l2 +[int(input(" ele : l2 "))]

for j in range(h):
    l3 =l3+[ l1[j]+l2[j]]
print(l3)
