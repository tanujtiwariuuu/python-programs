
'''program of fibbonacci number using recursion'''

def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)

# driver function
n=int(input("enter the number of terms in series "))
for i in range(n):
    print(fibbo(i),end=" ")