def binomialCoefficients(x, y, z) :
    C = x // (y*z)
    print(C) 

def factorials(n, m) :
    factN = 1
    factM = 1 
    factA = 1
    for i in range(1, n+1) :
        factN *= i
    for i in range(1, m+1) :
        factM *= i 
    a = n-m 
    for i in range(1, a+1) :
        factA *= i 

    binomialCoefficients(factN, factM, factA)

def main() :
    n, m = map(int, input().split())        # n is bigger than m
    if m > n:
        print("m cannot be greater than n for binomial coefficients.")
    else :
        factorials(n, m)

main()