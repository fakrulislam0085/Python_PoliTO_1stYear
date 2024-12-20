#code
total = 0.0
count = 0
inputStr = input("Enter the value:")

#use sentinel string to exit the loop
while inputStr != "":
    value = float(inputStr)
    total += value
    count += 1
    inputStr = input("Enter the value: ")

if count > 0 :
    average = total / count
else :
    average = 0.0
print("Average is:",average)