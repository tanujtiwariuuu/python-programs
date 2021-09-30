'''program to sort the word in alphabetic order'''

mystring=input("Enter a string ")
mylist=mystring.split()
print(sorted(mylist))

# method 2nd
mylist.sort()
print(mylist)
