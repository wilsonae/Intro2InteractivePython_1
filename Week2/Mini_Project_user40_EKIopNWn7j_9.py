# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# starting values for global variables
range_max = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, max_guesses
    if range_max == 100:
        max_guesses = 7
    else:
        max_guesses = 10
        
    secret_number = random.randrange(0,range_max)
    print "New game.  Guess a number between 0 and",range_max
    print "You have",max_guesses,"guesses.\n"

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_max, max_guesses
    range_max = 100
    max_guesses = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global range_max, max_guesses
    range_max = 1000
    max_guesses = 10
    new_game()
    
def input_guess(guess):
    global max_guesses	
    guess_number = int(guess)
    print "Your guess was",guess_number
    if guess_number == secret_number:
        print "Well done.  Your guess is Correct!\n"
    else:    
        if guess_number < secret_number:
            print "Your guess is too low."
        else:
            print "Your guess is too high."

        max_guesses = max_guesses -1
        if max_guesses > 0:
            print max_guesses, "guesses remaining.  Try again.\n"
            return
        else:
            print "You are out of guesses.  The correct answer was",\
            secret_number,"\n"
        
    new_game()

    
# create frame
frame = simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100",range100,150)
frame.add_button("Range: 0 - 1000",range1000,150)
guess = frame.add_input("Enter guess",input_guess,50)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
