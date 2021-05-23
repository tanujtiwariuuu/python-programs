num = int(input("enter a number : "))
i=0
rev=0
while num!=0:
    i=num%10
    rev = (rev*10)+i
    num=num//10
print(rev)