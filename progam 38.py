'''program to multiply two numbers'''

# by using inbuilt function
import numpy as np
r1=int(input("Enter the number of row of first matrix "))
c1=int(input("Enter the number of Column of first matrix "))
r2=int(input("Enter the number of row of second matrix "))
c2=int(input("Enter the number of column of second matrix "))
if c1!=r2:
    print("Multiplication is not possible ")
else:
    # taking the input of the matrix
    print("Enter the elements of the first matrix ")
    f_row=[]
    f_column=[]
    for i in range(r1):
        f_column = []
        for j in range(c1):
            n=int(input())
            f_column.append(n)
        f_row.append(f_column)

    print("Enter the elements of the second matrix ")
    s_row = []
    s_column = []
    for i in range(r2):
        s_column = []
        for j in range(c2):
            n = int(input())
            s_column.append(n)
        s_row.append(s_column)

    #final matrix
    c=[[0 for j in range(r1)] for i in range(c2)]
    # logic for multiplication
    for  i in range(r1):
       for j in range(c2):
           c[i][j]=0
           for k in range(c1):
               c[i][j]+=f_row[i][k]*s_row[k][j]
    print(c)


