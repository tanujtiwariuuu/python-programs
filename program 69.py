'''program to check if a string is a number (Float) '''

mystring=input("Enter a string ")

try:
    float(mystring)
    print("True")
except ValueError:
    print("False")