#input character
number = str(input("Enter number: "))
#input width
width = int(input("Enter width: "))
#add 0 to the beginning without using zfill()
zeroes = width
while len(number) < width:
    number = "0" + number
    zeroes += 1
#print output
print (number)