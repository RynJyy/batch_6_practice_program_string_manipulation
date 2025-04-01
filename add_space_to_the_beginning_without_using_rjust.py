#input character
statement = input("Enter statement: ")
#input width
width = int(input("Enter width: "))
#add space to the beginning without using rjust ()
space = width
while len(statement) < width:
    statement = "0" + statement
    space += 1
#print output
print (f'"{statement}"')