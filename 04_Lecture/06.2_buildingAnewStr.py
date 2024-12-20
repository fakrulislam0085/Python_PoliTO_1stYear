userInput = input("Enter the Credit Card Number: ")

creditCardNumber = ""

for char in userInput :
    if char == " " or char == "-" :
        continue
    else:
        creditCardNumber += char
    
print(f"Formatted Credit Card Number: {creditCardNumber}")