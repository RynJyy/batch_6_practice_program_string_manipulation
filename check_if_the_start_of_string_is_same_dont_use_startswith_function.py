#input character
character = input("Enter statement: ")
#input prefix
prefix = input("prefix: ")
#check if true or false dont use startswith()
if character[:len(prefix)] == prefix:
    print ("true")
else:
    print ("false")