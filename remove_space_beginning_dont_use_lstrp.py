#input name
name = input("Enter name: ")
#remove space at beginning dont use lstrip
while name.startswith(" "):
    name = name[1:]
#print name 
print(name)