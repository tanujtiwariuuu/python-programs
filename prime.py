num = int(input("enter : "))
for i in range(2,num//2):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")
