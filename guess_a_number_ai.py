import random
import math

# config
low = 1
high = 100
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
    print()
   

def show_credits():
    print("""
 _   __    _____                _____           
| | / /   | ___ \              |  _  \          
| |/ /    | |_/ /_   _  ___    | | | |___ _ __  
|    \    | ___ \ | | |/ _ \   | | | / _ \ '_ \ 
| |\  \   | |_/ / |_| |  __/   | |/ /  __/ | | |
\_| \_/   \____/ \__, |\___|   |___/ \___|_| |_|
                  __/ |                         
                 |___/                          
""")
    print()
    
def get_guess(current_low, current_high):

    current_low + current_high // 2
    
    
    pass

def pick_number():
    print("Pick a number in your head between " + str(low) + " and " + str(high))
    print()
    input("and I will try to guess it, press enter when you have the number.")

def check_guess(guess):
    """
    Ask the player if the computer's number was too high, too low,
    or just right.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    pass

def show_result():
    print("""
 _____             _              __   __             _    _             
/  __ \           | |             \ \ / /            | |  | |
| /  \/ ___   ___ | |              \ v /___  _   _   | |  | | ___  _ __  
| |    / _ \ / _ \| |               \ // _ \| | | |  | |/\| |/ _ \| '_ \ 
| \__/\ (_) | (_) | |  _   _   _    | | (_) | |_| |  \  /\  / (_) | | | |
 \____/\___/ \___/|_| (_) (_) (_)   \_/\___/ \__,_|   \/  \/ \___/|_| |_|""")

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
    current_low = low
    current_high = high
    result = -1
    
    pick_number()
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess)

        if result == -1:
            # adjust current high
            pass
        elif result == 1:
            # adjust current low
            pass
        else:
            pass

    show_result()

    

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



