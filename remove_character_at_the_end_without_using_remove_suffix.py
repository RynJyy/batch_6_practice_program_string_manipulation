#input statement
statement = input("Enter string: ")
suffix = input("Enter suffix: ")
#remove characters at beginning without using removesuffix()
if statement.endswith(suffix):
    statement = statement[:-len(suffix)]
#print statement
print (statement)


