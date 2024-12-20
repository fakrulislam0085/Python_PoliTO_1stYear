lowest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")

while inputStr != "" :
    value = int(inputStr)
    if value < lowest :
        lowest = value
    inputStr = input("Enter a value: ")
    
print(lowest)