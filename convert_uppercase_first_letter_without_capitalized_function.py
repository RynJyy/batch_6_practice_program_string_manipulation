#input statement
statement = input("Enter statement: ")
#capitalized the first letter without using capitalized
statement = statement[0].upper() + statement[1:].lower()
#print statement
print (statement)