def getLetterGrade(grade):
    if grade >= 3.85 :
        return 'A'
    elif grade >= 3.50 :
        return 'A-'
    elif grade >= 3.15 :
        return 'B+'
    elif grade >= 2.85 :
        return 'B'
    elif grade >= 2.5 :
        return 'B-'
    elif grade >= 2.15 :
        return 'C+'
    elif grade >= 1.85 :
        return 'C'
    elif grade >= 1.5 :
        return 'C-'
    elif grade >= 1.15 :
        return 'D+'
    elif grade >= 0.85:
        return 'D'
    elif grade >= 0.5:
        return 'D-'
    else:
        return 'F'

def main():
    grade = float(input("Enter a grade between 0.0 and 4.0: "))
    if 0.0 <= grade <= 4.0:
    #if grade >= 0.0 and grade<=4.0 
        letterGrade = getLetterGrade(grade)
        print(f"The corresponding letter grade is: {letterGrade}")
    else:
        print("Please enter a grade between 0.0 and 4.0.")

main()
