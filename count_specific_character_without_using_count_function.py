#input statement
statement = input("Enter statement: ")
#input what character to count
word = input("Enter word to count: ")
#count specific character without using count()
count = 0
for i in range(len(statement) - len(word) + 1):
    if statement[i:i + len(word)] == word:
        count += 1
#print output
print (count)