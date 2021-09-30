'''program to create a multiline string '''

from termcolor import colored
mystring=("this is first line\n"
          "this is second line \n"
          "this is third line\n")
print(mystring)


# method 2nd
str="this is first line\n"\
    "this iis second line\n"\
    "this is third line"
print(colored(str,'red'))