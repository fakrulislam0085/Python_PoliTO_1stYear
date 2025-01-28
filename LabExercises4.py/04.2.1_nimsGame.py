import random 

def is_power_of_two_minus_one(n) :
    power = 1
    while power - 1 < n:
        power *= 2
    return power - 1 == n


def computer_move_smart(n) :
    #check if the current number of marbles is a power of 2 minus 1 
    if is_power_of_two_minus_one(n) :
        return random.randint(1, n//2)
    else :
        #otherwise choose a number such that the remaining pile is a power of 2 minus 1 
        for i in range(n//2, 0, -1) :
            if is_power_of_two_minus_one(n-i) :
                return i
        return random.randint(1, max(n//2 , 1))

def computer_move_stupid(n) :
    return random.randint(1, max(n//2, 1)) 

def user_move(marbles) :
    while True :
        if marbles == 1 :
            return 1
        move = int(input(f"There are {marbles} marbles remaining. How many marbles do you want to take?: "))
        if move >= 1 and move <= marbles//2 :
            return move 
        else :
            print("Invalid move. You must take between 1 and m//2 marbles. Please try again!")

def game():
    #step-1 : generate the initial number of marbles
    marbles = random.randint(10, 100) 

    #step-2 : determine who goes first
    first_player = random.randint(0, 1) 

    #step-3 : determine if computer plays smart or stupid 
    computer_mode = random.randint(0, 1) 

    print(f"-------Welcome to the fucking Game!---------")
    print(f"The game starts with {marbles} marbles")

    #step-4 : play the game
    while marbles > 0 :
        #when user plays first 
        if first_player == 0 :  
            print(f"\n-----------------------")    
            print(f"\nYour Turn")
            move = user_move(marbles)
            marbles -= move     #update the number of marbles
            print(f"You took {move} marbles. Marbles left: {marbles}")
            if marbles == 0 :
                print(f"\n You took the last marbles, so you lost the game!")
                print(f"\n--------The Game Ends-----")
                break 
            first_player = 1   #switch to computer's turn

        #when computer plays first
        else :
            if computer_mode == 0 :
                print(f"\n-----------------------")  
                print(f"\nComputer's Turn(Stupid Mode)")
                move = computer_move_stupid(marbles)
            else :
                print(f"\n-----------------------")  
                print(f"\nComputer's Turn(Smart Mode)")
                move = computer_move_smart(marbles)

            marbles -= move   #update the number of marbles
            print(f"Computer took {move} marbles. Marbles left: {marbles}")
            if marbles == 0 :
                print(f"\nComputer took the last marbles, so it lost!")
                print(f"\n--------The Game Ends-----")
                break 
            first_player = 0    #switch to user's turn



if __name__ == "__main__" :
    game() 