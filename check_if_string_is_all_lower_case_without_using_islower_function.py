#input statement
statement = input("Enter statement: ")
#check if all characters is lower without using islower()
if statement == statement.lower():
    print ("true")
else:
    print ("false")