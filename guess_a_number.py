import random

#config
high= 100
low= 10

# helper functions
def get_guess():
    while True:
        guess = input("Guess a number:")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number")
#start game
rand = random.randint(1, 100)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + " .");

guess = -1
tries = 0
limit = 10

#play game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
        
    tries += 1

#game over
if guess == rand:
    print("Wow great you can guess a number")
else:
    print("How are you this bad at a simple game... the number was " + str(rand) + ".")
