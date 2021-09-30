''' program to merege two mails'''
mail=''
with open('name.txt','r') as name:
    with open('myfile.txt','r') as file:
        f=file.read()
        l=name.read()

print(f+l)