#upperCase, lowerCase and digit counts in a string
word = input("Write the string: ")

countUpperCase = 0
countLowerCase = 0
countDigit = 0
vowelCount = 0

for ch in word :
    if ch.isupper() :
        countUpperCase += 1
    elif ch.islower() :
        countLowerCase += 1
    elif ch.isdigit() :
        countDigit += 1
    if ch.lower() in 'aeiou' :      #making letters smaller so that the upperCase vowel does not exclude
        vowelCount += 1

print(f"{countLowerCase}\n{countUpperCase}\n{countDigit}\n{vowelCount}") 


#printing the position of vowels or uppercase or lowercase letters
sentence = input("Write the sentence: ")

for i in range(len(sentence)) :
    if sentence[i].upper() in 'AEIOU' :
        print(i, end=" ")   #the index number, not the letter


