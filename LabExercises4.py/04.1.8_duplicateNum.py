def printDuplicateAdjacent(dup_list) :
    print("Duplicate adjacent numbers: ")
    for i in range(len(dup_list)) :
        print(dup_list[i])


def main() :
    num = (input("Enter a number: "))
    endWith = ""
    num_list = []
    dup_list = []
    prev_num = None     #None is a special value in python that indicates no value
    duplicate_found = False

    while num != endWith :
        current_num = int(num)
        if current_num != prev_num :
            num_list.append(current_num)
            
            if duplicate_found :
                print("Duplicate adjacent numbers: ", prev_num)
                duplicate_found = False
        else :
            dup_list.append(current_num)
            duplicate_found = True 

        prev_num = int(num)
        num = input("Enter a number: ")

    printDuplicateAdjacent(dup_list)

main()