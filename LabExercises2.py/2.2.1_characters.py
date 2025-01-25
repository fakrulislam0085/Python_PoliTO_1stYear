word = input("Insert the String: ")
length = len(word)
last_starting_indx = length - 3

print(word[:3]+"..."+word[last_starting_indx :])