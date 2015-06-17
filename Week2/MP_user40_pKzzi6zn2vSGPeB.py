# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# starting value for global variables
# game default to guessing between 0 and 100.
range_max = 100

# helper function to start and restart the game
def new_game():
    ''' This function will start a Guess The Number game with
        a fixed number of guesses '''
    
    # specify global variables modified in this function
    #  secret_number: random integer in the range (0,range_max]
    #  max_guesses: maximum number of tries at guessing the secret_number
    global secret_number, max_guesses
    
    # As per challenge in the 2nd improvement section use log
    # and ceiling to get the maximum number of guesses
    max_guesses = int(math.ceil(math.log(range_max,2)))
    # old code below using if/else
    #if range_max == 100:
    #    max_guesses = 7
    #else:
    #    max_guesses = 10
        
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
    ''' function that get the guess and tests if it is 
        too low, too high or correct.  It also checks if all
        the guesses have been used up.
        If either the guess was correct or too many guesses 
        were used, it starts a new game.
    '''
    
    # specify global variabls modified in this function
    #  max_guesses: maximum number of tries at guessing the secret_number
    global max_guesses	
    
    # convert the user's input to an integer and print it out
    guess_number = int(guess)
    print "Your guess was",guess_number
    
    # if the guess was correct print out a congratulatory message
    if guess_number == secret_number:
        print "Well done.  Your guess is Correct!\n"
        
    # The guess was incorrect 
    else:    
        # See if it was too high or too low and tell the user.
        if guess_number < secret_number:
            print "Your guess is too low."
        else:
            print "Your guess is too high."
            
        # Now reduce the number of remaining guesses by one
        max_guesses = max_guesses -1
        
        # If more than zero guesses remain, tell the user and return
        if max_guesses > 0:
            print max_guesses, "guesses remaining.  Try again.\n"
            return
        
        # Out of guesses so inform the user and also tell them
        # what the secret_number was.
        else:
            print "You are out of guesses.  The secret number was",\
            secret_number,"\n"
    
    # Either correct or out of guesses so start a new game
    new_game()


# create frame
frame = simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100",range100,150)
frame.add_button("Range: 0 - 1000",range1000,150)
guess = frame.add_input("Enter guess",input_guess,50)

# call new_game 
new_game()
