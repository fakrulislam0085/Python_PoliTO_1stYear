def isPrime(num) :
    if num == 2 :
        print("It is a prime number") 
    elif num > 2 :
        prime = True
        for i in range(2, num) :
            if (num % i == 0 ) :
                prime = False
                break
        if prime :
            print("It is a prime number") 
        else :
            print("It is a composite number")
    else :   #num = 0 or num = 1
        print("It is not a prime number")
        
def main() :
    num = int(input("Enter a number: "))
    isPrime(num)

main()