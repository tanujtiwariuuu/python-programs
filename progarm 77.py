'''program to convert two list into dictionary'''

l1=[1,2,3,4]
l2=["rajnish",'tripathi','easy','coding']
dic={}
for i in range(len(l1)):
    dic[l1[i]]=l2[i]
print("The new dictionary \n",dic)