#input statement
statement = input("Enter statement: ")
#capitalized first letter of every words without using title function
capitalized_words = []

words = statement.split()
for word in words:
    capitalized_word = word[0].upper() + word[1:].lower()
    capitalized_words.append(capitalized_word)
#print statement
result = " ".join(capitalized_words)
print(result)