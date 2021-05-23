if __name__ == '__main__':
    lst = []
    count = 0
    
    t = 0
    m = []
    l = ""
    p = []
    temp = []
    n = int(input())

    for i in range(0, n):
        ele = [input(), float(input())]
        lst.append(ele)

    lst.sort(key=lambda x: x[1])
    for x in range(0, len(lst)):
        g = lst[0][1]
        if g in lst:
            cou = cou + 1
            if cou > 1:
                lst.pop(x)

    t = lst[0][1]
    for j in range(0, len(lst)):

        p = lst[j]
        if t == p[1]:
            m.append(p[0])
    m.sort()
    for i in m:
        l = i
        print(l)
