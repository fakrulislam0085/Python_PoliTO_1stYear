'''
not(A and B) = not A or not B
not(A or B) = not A and not B
'''
# Program to evaluate logical expressions and their negations using De Morgan's law
def evaluate_de_Morgran(x) :
    expr1_original = "not (x>0 and x<100)"
    expr1_demorgan = "not (x>0) or not (x<100)"
    expr1_truth_val = not (x>10 and x<100)

    expr2_original = "not (x>0 or x<100)"
    expr2_demorgan = "not (x>0) and not (x<100)"
    expr2_truth_val = not (x>10 or x<100)

    expr3_original = "not(x>0 or 100<x)"
    expr3_demorgan = "not (x>0) and not (100<x)"
    expr3_truth_val = not (x>0 or 100<x) 

    expr4_original = "not (x>0 and x<100 or x==-1)"
    expr4_demorgan = "not(x>0 and x<100) and not(x==-1)"
    expr4_truth_val = not (x>0 and x<100 or x==-1)

    print("I.",expr1_original, "->", expr1_demorgan, "=>", expr1_truth_val)
    print("II.",expr2_original, "->", expr2_demorgan, "=>", expr2_truth_val)
    print("III.",expr3_original, "->", expr3_demorgan, "=>", expr3_truth_val)
    print("IV.",expr4_original, "->", expr4_demorgan, "=>", expr4_truth_val)


def main() :
    x = int(input("Enter X: "))
    evaluate_de_Morgran(x)

main()