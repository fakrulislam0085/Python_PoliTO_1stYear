sentence = input("Write down the sentence: ")
upperCaseLetter = ""
evenPositionLetter = ""
underScoreString = list(sentence)   #strings are immutable in python so converting it into a list
numberOfNumericDigit = 0 
positionOfVowels = ""

for i, char in enumerate(sentence) :
    #task 1 - only the uppercase letter
    if char.isupper() == True :
        upperCaseLetter += char + " "
    
    #task 2 - letter in even positions in the string 
    if i%2 == 0 :
        evenPositionLetter += char + " "

    #taks 3 - string with underscore
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if char in vowels :
        underScoreString[i] = "-"

    #task 4 - number of numeric digits in the string
    if char.isdigit() == True :
        numberOfNumericDigit += 1

    #task 5 - position of vowels in the string
    if char in vowels :
        positionOfVowels += str(i) + " "

#converting our list to string
underScoreString = "".join(underScoreString)

print("Task 1: ", upperCaseLetter)
print("Task 2: ", evenPositionLetter)
print("Task 3: ", underScoreString)
print("Task 4: ", numberOfNumericDigit)
print("Task 5: ", positionOfVowels)

    