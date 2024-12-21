balance = 2000

def withdraw(amount) :
    #this function inteds to access the 'gloval' variablel
    global balance      #If you omit the global declaration, then the balance variable
                        #inside the withdraw function is considered a local variable
    if balance >= amount:
        balance = balance - amount
    print(balance)

def main() :
    amount = 10000 
    withdraw(amount)
main()
