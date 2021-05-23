i = int(input())
lis = list(map(int,input().split()))
lis.remove(max(lis))
print (max(lis))