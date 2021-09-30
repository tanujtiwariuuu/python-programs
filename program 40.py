# program to remove punctuations from a string

mystring=input("Enter a string ")
newstring=''
for i in mystring:
    if i==' ' or i==',' or i=='(' or i==')':
        continue
    else:
        newstring+=i
print("the new string is \n",newstring)