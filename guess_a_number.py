import random
import math

# config
low = 0
high = 20
limit = math.ceil(math.log(high, 2))


# helper functions
def show_start_screen():
        print("""
     _____                                                     _               
    |  __ \                                                   | |              
    | |  \/_   _  ___  ___ ___    __ _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
    | | __| | | |/ _ \/ __/ __|  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
    | |_\ \ |_| |  __/\__ \__ \ | (_| | | | | | |_| | | | | | | |_) |  __/ |   
     \____/\__,_|\___||___/___/  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                               
                                                                               """)

def show_credits():
    print("""
 _   __    _____                _____           
| | / /   | ___ \              |  _  \          
| |/ /    | |_/ /_   _  ___    | | | |___ _ __  
|    \    | ___ \ | | |/ _ \   | | | / _ \ '_ \ 
| |\  \   | |_/ / |_| |  __/   | |/ /  __/ | | |
\_| \_/   \____/ \__, |\___|   |___/ \___|_| |_|
                  __/ |                         
                 |___/                          """)
    
def get_guess():
    while True:
        guess = input("Guess a number: ")
        print()

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +" you have " + str(limit) + " guesses" + ".")
    print()

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        print()
    elif guess > rand:
        print("You guessed too high.")
        print()

def show_result(guess, rand):
    if guess == rand:
        print("""
 _____             _              __   __             _    _             
/  __ \           | |             \ \ / /            | |  | |            
| /  \/ ___   ___ | |              \ V /___  _   _   | |  | | ___  _ __  
| |    / _ \ / _ \| |               \ // _ \| | | |  | |/\| |/ _ \| '_ \ 
| \__/\ (_) | (_) | |  _   _   _    | | (_) | |_| |  \  /\  / (_) | | | |
 \____/\___/ \___/|_| (_) (_) (_)   \_/\___/ \__,_|   \/  \/ \___/|_| |_|""")
        print()
    else:
        print("""
 _   _                      _                         
| | | |                    | |                        
| |_| | __ _               | |     ___  ___  ___ _ __ 
|  _  |/ _` |              | |    / _ \/ __|/ _ \ '__|
| | | | (_| |  _   _   _   | |___| (_) \__ \  __/ |   
\_| |_/\__,_| (_) (_) (_)  \_____/\___/|___/\___|_| """)
        print()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()
        print()
        
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print()

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
