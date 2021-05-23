start = int(input("enter start : "))
last = int(input("enter last : "))
for i in range(start,last):
    for j in range(2,i):
        if i%j == 0:
            break

    else:
        print(i)
