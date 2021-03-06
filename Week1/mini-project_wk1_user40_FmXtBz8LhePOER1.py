# Rock-paper-scissors-lizard-Spock template
# http://www.codeskulptor.org/#user40_FmXtBz8LhePOER1.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#

# import the random module
import random

# helper functions

def name_to_number(name): 
    # convert name to number using if/elif/else
    if name == "rock" :
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        # Invalid name entered so return 99
        return 99


def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        return "rock" 
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        # this should never happen as the program controls the numbers
        return "Error: Number not in the range [0,4]"
     

def rpsls(player_choice): 
    # This simulates the Rock-paper-scissors-lizard-Spock game
    # where a player plays against the computer.  The computer
    # picks one of the choices at random.

    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # catch an invalid name
    if player_number == 99:
        print 'Error: Name not one of "rock", "paper", "scissors", "lizard", "Spock"'
        return

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice

    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5
    # difference means 
    #  0: both picked the same: tie
    #  1: player picked one further clockwise than computer: player wins
    #  2: player picked two further clockwise than computer: player wins
    #  3: player picked one further anti-clockwise than computer: computer wins
    #  4: player picked two further anti-clockwise than computer: computer wins
    # based on https://d396qusza40orc.cloudfront.net/interactivepython1/source_videos/week1-redo/rpsls.pdf

    # use if/elif/else to determine winner, print winner message
    if difference == 0:		# Player and computer tie
        print "Player and computer tie!"
    elif difference > 2:  	# This caters for 3 and 4 where the computer wins 
        print "Computer wins!"
    else:					# all that is left is 1 and 2 where the player wins
        print "Player wins!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


