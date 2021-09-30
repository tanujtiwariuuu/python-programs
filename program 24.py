# program to convert decimal to bianry , Hexa and octal number
bin=[]
def convert_bin(n):
    while n!=0:
        r =n%2
        bin.append(r)
        n=n//2
    for i in range(len(bin)-1,-1,-1):
        print(bin[i],end="")
# function for convert the decimal to octal
oct=[]
def convert_oct(n):
     while(n!=0):
         r=n%8
         oct.append(r)
         n=n//8
     for i in range(len(oct)-1,-1,-1):
         print(oct[i],end="")
# function for convert the decimal to hexadecimal
hex=[]
def convert_hex(n):
    while(n!=0):
        r=n%16
        if(r>9):
            if(r==10):
                hex.append("A")
            elif (r== 11):
                hex.append("B")
            elif (r == 12):
                hex.append("C")
            elif (r == 13):
                hex.append("D")
            elif (r== 14):
                hex.append("E")
            else:
                hex.append("F")
        else:
            hex.append(r)
        n=n//16
    for i in range(len(hex)-1,-1,-1):
        print(hex[i],end="")
# Driver function
n=int(input("Enter a number\n"))
print("The binary conversion is ",end="")
convert_bin(n)
print("\nThe Octal conversion is ",end="")
convert_oct(n)
print("\nThe Hexadecimal conversion is ",end="")
convert_hex(n)