number = input("Enter the 10 digit telephone number: ")

#Using Concatenation to re design our phone number
final_number = '(' + number[:3] + ')' + " " + number[3:6] + "-" + number[6:]

print(f"The formatted number is: {final_number}")
