'''program to check a key is already present in dictionary or not'''

dic={1:23,2:43,4:54,8:87}

key=int(input("Enter a key "))
if key in dic:
    print("Key is already in the dictionary")
else:
    print("Key is not present in dictionary")