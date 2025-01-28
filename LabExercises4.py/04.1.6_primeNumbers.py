def isPrime(num) :
    start = 3
    print(2)    #handle 2 separately   
    while start <= num :
        prime = True
        for i in range(2, start) :
            if (start % i == 0 ) :
                prime = False
                break
        if prime :
            print(start)
        start += 1

def main() :
    n = int(input()) 
    isPrime(n)
    
main()