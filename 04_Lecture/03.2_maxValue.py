largest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")

while inputStr != "" :
    value = int(inputStr)
    if value > largest :
        largest = value
    inputStr = input("Enter a value: ")
    
print(largest)