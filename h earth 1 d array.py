args = input()
temp =""
s=""
# for i in range(ord("("),ord(")")+1):
for i in range(0,len(args)):
    if args[i]=="(":
        temp=temp+args[i]
    elif args[i] == ")":
        s=s+args[i]
if len(temp)==len(s):
    print(len(temp))
else:
    print(0)