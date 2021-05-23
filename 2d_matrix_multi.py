n = int(input("enter no. of rows : "))
m = int(input("enter no. of columns : "))
l2 = []
l4 = []
l3 = []
g = []
l5 = []
print('enter l1 : ')
for i in range(n):
    l1 = list(map(int, input().split()))
    l2 = l2+[l1]
print('enter l1 : ')
for i in range(n):
    l1 = list(map(int, input().split()))
    l3 = l3 + [l1]
t = q = 0
for i in range(n):
    s = 0
    for j in range(m*m):
        t = j % m
        g = l2[i][t]
        if j == m:
            s = s+1
        q = g*l3[t][s]
        l4.append(q)
for i in range(0, len(l4), m):
    total = 0
    total = sum(l4[i:m+i:])
    l5.append(total)
print(l5)
