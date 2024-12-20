value = int(input("Enter a Number: "))
inputStr = input("Enter a number: ")

while inputStr != "" :
    previous = value 
    newVal = int(inputStr)
    if previous == newVal :
        print("Duplicate Detected")
        break
    inputStr = input("Enter a number: ")