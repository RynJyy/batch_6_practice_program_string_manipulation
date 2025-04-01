#input statement
statement = input("Enter statement: ")
#input word to find
word = input("Enter word to find: ")
#find the first location of the word in statement starting from last character without using rindex()
position = -1
for i in range(len(statement)):  
    if statement[i:i + len(word)] == word:
        position = i
#print output
if position != -1:
    print(position)
else:
    print("Substring not found")