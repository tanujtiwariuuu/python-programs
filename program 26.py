# program to find the HCF

'''function for finding the GCD'''
def GCD(n1,n2):
    # ternary operator
    least=n1>n2 and n2 or n1
    while least!=1:
        if n1%least==0 and n2%least==0:
            return least
        else:
            least-=1
    return 1

# driver program
n1=int(input("Enter first number"))
n2=int(input("Enter Second number"))
print("GCD of ",n1," and ",n2 ," is ",GCD(n1,n2))

