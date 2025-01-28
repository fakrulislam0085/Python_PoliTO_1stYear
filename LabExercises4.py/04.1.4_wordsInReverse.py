readTheWord = input("Write a word: ")

backWord = readTheWord[::-1]
capitalFromBack = ""
for char in backWord :
    if char.isupper() :
        capitalFromBack += char
    
print(backWord)
print(capitalFromBack)