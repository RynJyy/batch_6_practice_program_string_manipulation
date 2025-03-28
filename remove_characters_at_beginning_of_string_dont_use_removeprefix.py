#input statement
statement = input("Enter string: ")
prefix = input("Enter prefix: ")
#remove characters at beginning without using removeprefix()
if statement.startswith(prefix):
    statement = statement[len(prefix):]
#print statement
print (statement)
