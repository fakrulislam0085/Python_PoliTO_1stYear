#code
inputSTr = input("Enter value: ")
negatives = 0


while inputSTr != "" :
    Value = int(inputSTr)
    if Value < 0 :
        negatives += 1
    inputSTr = input("Enter the value: ")

print("There are", negatives, "negative Values!")
