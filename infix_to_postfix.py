m = ''
expr = input('expression : ')
precedence = {"+": 1, '-': 1, '*': 2, '/': 2, '(': 4, ')': 4, '^': 3}
operator = '*-+/()^'
t = ''
for i in range(len(expr)):
    if expr[i] in operator:

    else:
        t += expr[i]
top=-1
def stack(arr,ele):
    global top
    top += 1
