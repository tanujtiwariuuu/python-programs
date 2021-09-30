# program to find the factors of the given numbers

n=int(input("Enter a number"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")