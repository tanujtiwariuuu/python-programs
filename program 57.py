'''program to copy a file '''

with open('name.txt','r') as name:
    line=name.read()
    with open('copy.txt','w') as copy:
        copy.write(line)
