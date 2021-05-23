def reverse_number(number):
    # i=0
    rev = 0
    rem = 0
    while (number!=0):
        rem = number %10
        rev = (rev*10)+rem
        number=number//10
    return rev
print(reverse_number(5624437637271654))

