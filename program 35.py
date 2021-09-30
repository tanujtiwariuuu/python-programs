# program to find the binary of a number by using recursion

def con_bin(n):
    if n==0:
        return
    else:
        con_bin(n//2)
        print(n%2,end="")

# driver program
n=int(input("Enter a number "))
print("Binary of the number is ",end="")
con_bin(n)