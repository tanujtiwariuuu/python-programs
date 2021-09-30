'''program to make a flattened list from a nested list'''

mylist=[[1,2,3,4],[3,4,5,6],[6,7,8,9]]

flat_list=[]
for i in mylist:
    for j in i:
        flat_list.append(j)
print(flat_list)