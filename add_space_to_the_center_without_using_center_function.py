#input character
characters = input("Enter statement: ")
#input how many spaces should be added
spaces = int(input("Enter number of spaces: "))
#add space without using the center function
middle_characters = len(characters) // 2
added_spaces_characters = characters[:middle_characters] + " " * spaces + characters[middle_characters:]
#print output
print (added_spaces_characters)
