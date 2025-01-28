
def identifySeason(m, d) :
    if m == 1 or m == 2 or m == 3 :
        if m%3 == 0 and d >= 21 :
            season = "Spring"
        else :
            season = "Winter"

    elif m in [4, 5, 6]:
        if m%3 == 0 and d >= 21 :
            season = "Summer"
        else:
            season = "Spring"

    elif m in [7, 8, 9] :
        if m%3 == 0 and d >= 21 :
            season = "Fall"
        else :
            season = "Summer"

    else :
        if m%3 == 0 and d >= 21 :
            season = "Winter"
        else :
            season = "Fall"
    
    print(season)


def main() :
    month = int(input("Enter the month's number: "))
    day = int(input("Enter the day: "))

    identifySeason(month, day)

main()