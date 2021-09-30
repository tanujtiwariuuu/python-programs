# program to find the LCM of two numbers

'''Function for finding LCM of two numbers'''
def find_LCM(n1,n2):
    # ternary operator
    max=n1 >n2 and n1 or n2
    while(1):
        if max%n1==0 and max%n2==0:
            return  max
        max+=1


# Driver program
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
print(f"LCM of {n1} and {n2 } is {find_LCM(n1,n2)}")