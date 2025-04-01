#input string
string = input("Enter statement: ")
#remove space without using rstrip
while string.endswith(" "):
    string = string[:-1]
#print string
print (f'"{string}"')