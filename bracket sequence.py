str1 = input()
count = 0
min=100
bal=0
for i in range(0,len(str1)):
    if str1[i]==')':
        count=count-1
    else:
        count=count+1
    if min>count:

        min=count
        bal=0

    if min==count:
        bal=bal+1

if count==0:
   print(bal)
else:
   print("0")
