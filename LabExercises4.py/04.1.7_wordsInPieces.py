def wordsInPieces(word) :
    substrings = []

    for i in range(len(word)) :
        for j in range(i+1, len(word)+1) :
            substrings.append(word[i:j])    #in slicing string, j is exclusive so we need to write len(word)+1

    sorted_substrings = sorted(substrings, key=len)
    print("Substring of the give words are: ")
    for string in sorted_substrings :
        print(string)

def main() :
    word = input("Write the word: ")
    wordsInPieces(word)

main() 