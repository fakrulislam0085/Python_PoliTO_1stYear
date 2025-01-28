def square(side) :
    for i in range(side) :
        print('*' * side)
    print()
    
def rhombus(side) :
    line = (side * 2) - 1 
    spaces = side - 1 
    stars = 1
    
    
    for i in range(line) :
        if i < side :
            print(spaces * " " + stars * '*')
            if i == side - 1 :
                continue
            else :
                stars += 2 
                spaces -= 1 
        else :
            spaces += 1 
            stars -= 2 
            print(spaces* " " + stars * '*')


def main() :
    side = int(input("Enter the side of the square: "))
    square(side) 
    rhombus(side)


if __name__ == "__main__" :
    main()