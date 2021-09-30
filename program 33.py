'''program to find the sum of natural numbers using recursion'''

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

# driver program
n=int(input("Enter a number "))
print("The sum of the numbers upto ",n," is ",sum(n))