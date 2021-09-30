# program to find the power of 2 by ananymous function
'''Ananymous function :-
                         Anonymous functions can be used as an argument to other functions .example : lambda function'''
x=lambda x: 2**x
n=int(input("Enter the number of terms "))
for i in range(n):
    print(x(i))
