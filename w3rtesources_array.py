# 1. program to display:
# 1 2 3
# 4 5 6
# 7 9 8

# l1 = []
# num = int(input())
# for i in range(num):
#     l2 = []
#     for j in range(num):
#         l2 += [int(input())]
#     l1 += [l2]
# for i in range(num):
#     for j in range(num):
#         print(l1[i][j], end=' ')
#     print()

# program no. 106 at w3 resources array
# The given array is: 0 3 3 3 0 0 7 7 0 9
# The new array is: 6 3 14 9 0 0 0 0 0 0
# l1 = list(map(int, input().split()))
# l2=l1[::]
# for i in range(len(l1)-1):
#     if l2[i] == 0:
#         l2.remove(0)
#         l2.append(0)
#     if l2[i] == l2[i+1]:
#         l2[i+1] = 0
#         l2[i] = 2*l2[i]
# print(l2)

# program 104
l1 = list(map(int, input().split()))
for i in range(len(l1)-1):
    if i % 2 == 0:
        if l1[i] < l1[i+1]:
            pass
        else:
            l1[i], l1[i+1] = l1[i+1], l1[i]
    else:
        if l1[i]<l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i]
print(l1)
