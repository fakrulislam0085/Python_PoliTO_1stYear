number = input("Insert the telephone number: ")

#Using Concatenation to re design our phone number
final_number = '(' + number[:3] + ')' + " " + number[3:6] + "-" + number[6:]

print(final_number)