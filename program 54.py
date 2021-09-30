'''program to sort a dictionary by value'''

dic={1:"rajnish",4: "tripathi",3:"mahesh",2:"shadab"}


print(dict(sorted(dic.items(),key=lambda x:x[1])))