# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# starting value for global variables
#  range_max: upper limit for the range of guesses
#  initial value set to 100 for guessing between 0 and 100.
range_max = 100


# helper function to start and restart the game
def new_game():
    ''' This function will start a Guess The Number game with
        a fixed number of guesses '''
    
    # specify global variables modified in this function
    #  secret_number: random integer in the range (0,range_max]
    #  max_guesses: maximum number of tries at guessing the secret_number
    global secret_number, max_guesses
    
    # As per challenge in the 2nd improvement section use log and
    # ceiling from the math package to get the maximum number of guesses
    max_guesses = int(math.ceil(math.log(range_max,2)))
    #
    # original max_guesses code using if/else
    # if range_max == 100:
    #     max_guesses = 7
    # else:
    #     max_guesses = 10
        
    # get a random number between 0 and range_max
    secret_number = random.randrange(0,range_max)
    
    # print out start messages
    print "New game.  Guess a number between 0 and",range_max
    print "You have",max_guesses,"guesses.\n"


# define event handlers for control panel
def range100():
    ''' button that changes the range to [0,100) and starts a new game '''
    
    # specify global variable modified in this function
    #  range_max: upper limit for the range of guesses
    global range_max
    range_max = 100
    
    # start new game
    new_game()


def range1000():
    ''' button that changes the range to [0,1000) and starts a new game '''

    # specify global variable modified in this function
    #  range_max: upper limit for the range of guesses
    global range_max
    range_max = 1000
    
    # start new game
    new_game()


def input_guess(guess):
    ''' function that tests if the guess is too low, too 
        high or correct.  It also checks if all the guesses 
        have been used up.
        If either the guess was correct or too many guesses 
        were used, it starts a new game.
    '''
    
    # specify global variable modified in this function
    #  max_guesses: maximum number of tries at guessing the secret_number
    global max_guesses	
    
    # convert the user's input to an integer and print it out
    guess_number = int(guess)
    print "Your guess was",guess_number
    
    # test if the guess was correct 
    if guess_number == secret_number:
        # Correct guess: print out a congratulatory message
        print "Well done.  Your guess is Correct!\n"
        
    # Incorrect guess 
    else:    
        # Inform the user whether the secret number was higher 
        #  or lower than their guess.
        if guess_number < secret_number:
            print "The secret number is higher."
        else:
            print "The secret number is lower."
            
        # Reduce the number of remaining guesses by one
        max_guesses = max_guesses -1
        
        if max_guesses > 0:
            # If more than zero guesses remain, inform the user and continue
            print "You have",max_guesses, "guesses remaining.  Try again.\n"
            return
        
        else:
            # Out of guesses: inform the user and also tell them
            # what the secret_number was.
            print "You are out of guesses.  The secret number was",\
            secret_number,"\n"
    
    # Either correct or out of guesses so start a new game
    new_game()


# Create the frame
frame = simplegui.create_frame("Guess the Number",200,200)

# Create event handlers
# register button control elements
frame.add_button("Range: 0 - 100",range100,150)
frame.add_button("Range: 0 - 1000",range1000,150)
# register text input box
guess = frame.add_input("Enter guess",input_guess,50)

# Start frame
frame.start()

# Start the game
new_game()
