total=int(input("enter : "))
sym = input("symbol : ")
num = int(input("enter a number: "))
while True:

    sym = input("symbol : ")
    if sym == "=":
        print(total)
        break
    elif sym =="+":
        total = total+num
    elif sym== "-":
        total = total-num
    elif sym == "*":
        total=total*num

    num = int(input("enter a number: "))