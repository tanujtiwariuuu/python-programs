'''program to split a list in to equal size of chunks'''

mylist=[1,2,3,4,5,6,7,8,9,0]

# let's we have to divides the list into size of 2
for i in range(len(mylist)):
    t=1
    l=[]
    while t<=2:
       l.append(mylist[i])
       i+=1
       if(i==len(mylist)):
           break
       t+=1
    print(l)

# method 2nd

print("this is by second method ")
for i in range(0,len(mylist),3):
    x=i
    print(mylist[x:x+3])