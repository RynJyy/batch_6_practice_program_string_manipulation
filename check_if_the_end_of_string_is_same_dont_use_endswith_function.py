#input character
character = input("Enter statement: ")
#input suffix
suffix = input("suffix: ")
#check if true or false (dont use endswith())
if character[len(character) - len(suffix):] == suffix:
    print ("true")
else:
    print ("false")

    