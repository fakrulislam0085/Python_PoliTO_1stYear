def evaluate_expression(x) :
    expr1 = x > 0 and x < 100
    expr2 = x > 0 or x < 100
    expr3 = x > 0 or x > 100
    expr4 = x > 0 and x < 100 or x == -1

    print("I. x > 0 and x < 100 => ", expr1)
    print("II. x > 0 or x < 100 => ", expr2)
    print("III. x > 0 or 100 < x => ", expr3)
    print("IV. x > 0 and x < 100 or x == -1 =>", expr4)

def main() :
    x = int(input("Write x: "))
    evaluate_expression(x)

main()

