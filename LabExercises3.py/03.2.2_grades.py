
def finalResult(A, B, C, D, F, grade) :
    #Applying condition according to user input
    if grade == 'A' :
        print("G.P.A -", A)
    elif grade == 'A+' or grade == 'a+':
        print("G.P.A -", A)
    elif grade == 'A-' or grade == 'a-':
        print("G.P.A -", A - 0.3)
    elif grade == 'B' :
        print("G.P.A -", B)
    elif grade == 'B+' or grade == 'b+':
        print("G.P.A -", B + 0.3)
    elif grade == 'B-' or grade == 'b-':
        print("G.P.A -", B - 0.3)
    elif grade == 'C' :
        print("G.P.A -", C)
    elif grade == 'C+' or grade == 'c+':
        print("G.P.A -", C + 0.3)
    elif grade == 'C-' or grade == 'c-':
        print("G.P.A -", C - 0.3)
    elif grade == 'D' :
        print("G.P.A -", D)
    elif grade == 'D+' or grade == 'd+':
        print("G.P.A -", D + 0.30)
    elif grade == 'D-' or grade == 'd-':
        print("G.P.A -", D - 0.3)
    elif grade == 'F+' or grade == 'F-' or grade == 'f+' or grade == 'f-':
        print("The grades 'F+/f+' and 'f+/f-' do not exist")
    else:
        print ("There is an error in input or the grade does not exist!")

def gradeSystem(grade) :
    #decorating our output
    print("-------------------------")

    #storing the numerical value of Grade
    A = 4.00
    B = 3.00
    C = 2.00
    D = 1.00
    F = 0.00
    
    finalResult(A, B, C, D, F, grade)      #Calling the finalResult function

def main() :
    grade = input("Take user input:")
    gradeSystem(grade)      #calling the gradeSystem function

main()