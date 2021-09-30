# progra to find the number of vowels

mystring=input("Enter the string  ")
dic={'a':0 ,'e':0,'i':0,'o':0,'u':0}
for i in mystring:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i' :
        dic[i]+=1
print(dic)