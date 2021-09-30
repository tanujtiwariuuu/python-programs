'''program to check whether a string is palindrome or not'''

mystring=input("Etner a string ")
l=len(mystring)
for i in range(l//2+1):
    if mystring[i]!=mystring[l-i-1]:
        print("String is not a palindrome string")
        break
else:
    print("string is a palindrome string")

