l = [4,6,0,7,5,8,9,3,5,7,1]

temp = []
for i  in  range(0,len(l)-1):
    if l[i]:
        i= 0
        while i!=len(l)-1 :
            if l[i]<=l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp




            i=i+1

print(l)

