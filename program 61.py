'''program to parse a string into float or int '''

mystring=input("Enter a string")

parse_str=int(mystring)

print("Number after parsing  :",parse_str," and class of it is ",type(parse_str) )

parse_float=float(mystring)
print("Number after parsing in float :",parse_float," and class of it is ",type(parse_float) )