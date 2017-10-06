import math

# config
print("Hello summoner, what is your name?")
name = input()
print()
print("Now enter your select high and low numbers " + name + ".")
print()
print("Enter Low")
print()
low = input()
low = int(low)
print("Enter High")
print()
high = input()
high = int(high)
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
                                                                       
___  ___          _         ______                                     
|  \/  |         | |        | ___ \                                    
| .  . | __ _  __| | ___    | |_/ /_   _                               
| |\/| |/ _` |/ _` |/ _ \   | ___ \ | | |                              
| |  | | (_| | (_| |  __/   | |_/ / |_| |                              
\_|  |_/\__,_|\__,_|\___|   \____/ \__, |                              
                                    __/ |                              
                                   |___/                               
 _____                                  _____                          
/  __ \                                |  _  |                         
| /  \/ ___  _ __  _ __   ___  _ __    | | | |_ __                     
| |    / _ \| '_ \| '_ \ / _ \| '__|   | | | | '_ \                    
| \__/\ (_) | | | | | | | (_) | |      \ \_/ / | | |                   
 \____/\___/|_| |_|_| |_|\___/|_|       \___/|_| |_|                   
                                                                       
                                                                       
 __  _____    _______         ____     _______  _____  __   ______     
/  ||  _  |  / / __  \       / ___|   / / __  \|  _  |/  | |___  /     
`| || |/' | / /`' / /'______/ /___   / /`' / /'| |/' |`| |    / /      
 | ||  /| |/ /   / / |______| ___ \ / /   / /  |  /| | | |   / /       
_| |\ |_/ / /  ./ /___      | \_/ |/ /  ./ /___\ |_/ /_| |_./ /        
\___/\___/_/   \_____/      \_____/_/   \_____/ \___/ \___/\_/               
                                                                    
                                                                     
                                                                                           
                                                                                           
""")
    print()
    
def get_guess(current_low, current_high):

    return (current_low + current_high) // 2
    
def pick_number():
    print("Alright " + name + " Pick a number in your head between the numbers that you chose and I will try to guess it in "
          + str(limit) + " tries or less.")
    print()
    input("Press 'Enter' to continue " + name)
    print()
def check_guess(guess , tries):
    
    print("(Guess " + str(tries) + " of " + str(limit) + ") Was your number " + str(guess) + "?")
    print()
    print("Do I need to go Higher, Lower or was I Correct, DONT CHEAT " + name + " IM TRUSTING YOU!")
    print()
    answer = input()
    answer = answer.lower()
    if answer == 'higher' or answer == 'h':
        return -1
    elif answer == 'lower' or answer == 'l':
        return 1
    elif answer == 'correct' or answer == 'c':
        return 0
    else:
        print()
        print("You need to enter 'higher', 'lower' or 'correct'")
        print()
                             
        
    
    
    

def show_result():
    print("""
 _____     _    _                                _                         
|_   _|   | |  | |                              | |                        
  | |     | |  | | ___  _ __                    | |     ___  ___  ___ _ __ 
  | |     | |/\| |/ _ \| '_ \                   | |    / _ \/ __|/ _ \ '__|
 _| |_    \  /\  / (_) | | | |   _    _    _    | |___| (_) \__ \  __/ |   
 \___/     \/  \/ \___/|_| |_|  (_)  (_)  (_)   \_____/\___/|___/\___|_|   
                                                                             """)

def play_again():
    while True:
        decision = input("I guessed the number in less than " + str(limit) + " guesses. Would you like to play again " + name + "? (y/n)")
        decision = decision.lower()
        print()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n' " + name + ".")
            print()

def play():
    current_low = low
    current_high = high
    result = -1
    tries = 0
    
    pick_number()
    
    while result != 0 and tries < limit:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess, tries)

        if result == -1:
            current_low = guess + 1
        elif result == 1:
            current_high = guess - 1

        tries += 1
    show_result()

    

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



