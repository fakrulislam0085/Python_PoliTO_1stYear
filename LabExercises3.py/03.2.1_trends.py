def trends(a, b, c) :
    if a < b < c :
        print("Strictly Increasing")
    elif a > b > c :
        print("Strictly Decreasing")
    else :
        print("Neither")


def main() :
    a, b, c = map(int, input().split()) 
    trends(a, b, c)

main()