def findOutLeapyear(y) :
    #If at least one condition is true then return true 
    if (y%4 == 0 and y%100 != 0) or (y%400 == 0) :      
        return True 
    else :
        return False


def main() :
    year = int(input("Write a year (greater than 1582): "))
    if year <= 1582:
        print("Please enter a year greater than 1582.")
    else :
        result = findOutLeapyear(year)
        if result :
            print(f"{year} is a leap year")
        else :
            print(f"{year} is not a leap year")

main()