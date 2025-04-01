#input statement
statement = input("Enter statement: ")
#input word to find
word = input("Enter word to find: ")
#find word in statement without using index()
position = 0
for i in range(len(statement)):
    if statement[i:i+len(word)] == word:
        position = i
        break
#print output
if position != -1:
    print(position)
else:
    print("Substring not found")

    