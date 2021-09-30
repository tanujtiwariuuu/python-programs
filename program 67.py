'''progarm to read a file line by line'''

from termcolor import  colored
with open('name.txt','r') as name:
    while True:
        l=name.readline()
        if l=='':
            break
        print(colored(l.strip(),'red'))

