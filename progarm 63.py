'''program to convert the string into datetime'''

from dateutil import parser
mystring=input("Enter a time in string formate") # sep 6 2021 03:03:12 AM
datetime=parser.parse(mystring)
print(datetime)
print(type(datetime))
