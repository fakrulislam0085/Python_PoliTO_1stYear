
string = input("Write the word: ")

#checking letter
if string.isalpha() :
    print("It contains only letters")
elif string.isalnum() :
    print("It contains letters and digits")

#checking first char
if string[0].isupper():
    print("It starts with a capital letter")
    if string.isupper() :
        print("It contains only capital letters")

elif string[0].islower():
    print("It starts with a small letter")
    if string.islower() :
        print("It contains only lowercase letters")

elif string[0].isdigit():
    print("It starts with a digit")
    if string.isdigit() :
        print("It contains only decimal numeric digits")


#checking the last char
if string.endswith(".") :
    print("It ends with a period")

# Check if the string contains both lowercase letters and digits
if any(c.islower() for c in string) and any(c.isdigit() for c in string):
    print("It contains lowercase letters and digits")

# Check if the string contains both uppercase letters and digits
if any(c.isupper() for c in string) and any(c.isdigit() for c in string):
    print("It contains uppercase letters and digits")



