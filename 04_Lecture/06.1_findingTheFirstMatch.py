#find the position of the first digit in a string
string = input("Write the string: ")
found = False
position = 0

while not found and position < len(string) :       #if true && true meet, the loop continues
    if string[position].isdigit() :
        found = True
    else:
        position += 1

if found == True :
    print("First digit occurs at position:",position)
else :
    print("The string does not contain a digit.") 



#find the position of the last digit in a string
found = True
pos = len(string) - 1

while found and pos >= 0 :      #if true && true meet, the loop continues
    if string[pos].isdigit() :
        found = False
    else :
        pos -= 1

if found == False :
    print("The last digit occurs at position:", pos)
else:
    print("There is no digit in the string")

