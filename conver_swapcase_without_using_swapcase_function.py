#input characters
statement = input("Enter statement: ")
#convert to swapcase without using swapcase function
swap_statement = ""
for i in statement:
    if i.islower():
        swap_statement += i.upper()
    elif i.isupper():
        swap_statement += i.lower()
    else:
        swap_statement += i
#print output
print(swap_statement)