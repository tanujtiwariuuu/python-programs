num = int(input("enter a number : "))
i=0
t=num
rev=0
while num!=0:
    i=num%10
    s=i**3
    print(s)
    rev = rev+s
    num=num//10
if rev == t:
    print("ermstrong")
else:
    print("not armstrong")
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             print(i)
#             break