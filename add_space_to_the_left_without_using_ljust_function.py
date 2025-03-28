#input statement
statement = input("Enter statement: ")
#input width
width = int(input("Enter total width: "))
#add space to the left without using ljust
space = width
while len(statement) < width:
    statement = statement + " "
    space += 1
#print output
print (f'"{statement}"')