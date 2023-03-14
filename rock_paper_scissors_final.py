# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:08:52 2022

@author: Mateusz Kus for a course - Object Oriented Programming - McMaster
"""

'''
This is a program to play the game: Rock Paper Scissors Spock Lizard

Rules of the game are:
    
- Spock beats scissors and rock, but loses to paper and lizard.
- Lizard beats Spock and paper, but loses to rock and scissors.
- Rock beats scissors and lizard, but loses to paper and Spock.
- Paper beats rock and Spock, but loses to scissors and lizard.
- Scissors beats paper and lizard, but loses to rock and Spock.

The program will have two players and each of them produce a random outcome, i.e., Rock, paper, scissor, spock, or lizard. 

Random number generator will select options:
    1 - Spock
    2 - Lizard
    3 - Rock
    4 - Paper
    5 - Scissors

Based on each player’s outcome, winner is determined.

You will see current score after each round, and score will be summed up if you decide to play more rounds.
You will have option to replay the game as many times as you want.

'''

#importing random to be able to use in the function select_random_value()
import random

#naming variables and assigning names
ROCK = 'Rock'
PAPER = 'Paper'
SPOCK = 'Spock'
SCISSORS = 'Scissors'
LIZARD = 'Lizard'

#setting zero scores for the start of the game
player1_score = 0
player2_score = 0

#main function that runs other functions
def main():
    '''
    Main function of the game that starts all the other functions.

    Returns
    -------
    None.

    '''
    
    #declaring global variables for score counting in local scope
    global player1_score
    global player2_score
    
    #randomly selecting values for the game (Rock, Paper, etc.) for each player
    player1 = select_random_value()
    player2 = select_random_value()
    
    #printing randomly selected values on the screen
    print('\nPlayer one selected: ' + player1[1])
    print('Player two selected: ' + player2[1])
    
    #selecting the winner based on the selection and adding points to each players score
    winner = selecting_winner(player1[1], player2[1])
    
    #new scores for each player
    player1_score = winner[0]
    player2_score = winner[1]
    
    #printing current score on the screen
    print(f'\nCurrent score is\n---------------------------\nPlayer 1: {winner[0]}\nPlayer 2: {winner[1]}')
    
    # asking player to play again or not. If yes selected, game will restart, otherwise it will say thanks and exit.
    play_again(input('Press \'y\' and ENTER if you want to play again, otherwise just press ENTER: '))

#function to select random value and assign text
def select_random_value():
    '''
    Random selection of option from 6 possibilities for each player in the game.

    Returns
    -------
    random_value : int
    description : str

    '''
    description = ''
    random_value = random.randint(1, 5)
    if random_value == 1:
        description = SPOCK
    if random_value == 2:
        description = LIZARD
    if random_value == 3:
        description = ROCK
    if random_value == 4:
        description = PAPER
    if random_value == 5:
        description = SCISSORS
        
    return random_value, description

#function that decides who wins and prints output
def selecting_winner(player1_selection, player2_selection):
    
    '''
    Parameters
    ----------
    Each player's random selection is the input (as string) from available options (Rock, Paper, etc....)
    player1_selection : str
    player2_selection : str
    
    Returns
    -------
    Returns the results of another function that calculate scores and adds it to total score (increment_counter())

    '''
    #declaring global variables for score in the local scope.
    global player1_score
    global player2_score
    
    #option for draw if both players selected same option
    if player1_selection == player2_selection:
        print('It is a draw')
    
    #Options for selecting winner
    
    # SPOCK for player 1
    #win
    
    if player1_selection == SPOCK and (player2_selection == SCISSORS or player2_selection == ROCK):
        print('Player 1 wins')
        return increment_counter(1, player1_score, player2_score)
    
    #loss
    
    if player1_selection == SPOCK and (player2_selection == PAPER or player2_selection == LIZARD):
        print('Player 2 wins')
        return increment_counter(2, player1_score, player2_score)
    
    # LIZARD for player 1
    
    #win
    if player1_selection == LIZARD and (player2_selection == SPOCK or player2_selection == PAPER):
        print('Player 1 wins')
        return increment_counter(1, player1_score, player2_score)
    
    #loss
    if player1_selection == LIZARD and (player2_selection == ROCK or player2_selection == SCISSORS):
        print('Player 2 wins')
        return increment_counter(2, player1_score, player2_score)
    
    # ROCK for player 1
    
    #win
    if player1_selection == ROCK and (player2_selection == SCISSORS or player2_selection == LIZARD):
        print('Player 1 wins')
        return increment_counter(1, player1_score, player2_score)
    
    #loss
    if player1_selection == ROCK and (player2_selection == PAPER or player2_selection == SPOCK):
        print('Player 2 wins')
        return increment_counter(2, player1_score, player2_score)
        
    # PAPER for player 1
    
    #win
    if player1_selection == PAPER and (player2_selection == ROCK or player2_selection == SPOCK):
        print('Player 1 wins')
        return increment_counter(1, player1_score, player2_score)
    
    #loss
    if player1_selection == PAPER and (player2_selection == SCISSORS or player2_selection == LIZARD):
        print('Player 2 wins')
        return increment_counter(2, player1_score, player2_score)

    # SCISSORS for player 1
    
    #win
    if player1_selection == SCISSORS and (player2_selection == PAPER or player2_selection == LIZARD):
        print('Player 1 wins')
        return increment_counter(1, player1_score, player2_score)
    
    #loss
    if player1_selection == SCISSORS and (player2_selection == ROCK or player2_selection == SPOCK):
        print('Player 2 wins')
        return increment_counter(2, player1_score, player2_score)
    
    #in case there is a draw, calling other function to count scores
    return increment_counter(0, player1_score, player2_score)

#increment counter function to count score of each player based on round results                      

def increment_counter(winner, player1_current_score, player2_current_score):
    '''

    Parameters
    ----------
    winner : int
        supply numbe of the winner 1 for player 1 and 2 for player 2, 0 if this is a draw
    player1_current_score : float
        supply current score for player 1
    player2_current_score : TYPE
        supply current score for player 2

    Returns
    -------
    player1_new_score : float
        returns new score of player 1
    player2_new_score : float
        returns new score of player 2

    '''
    #if player one wins
    if winner == 1:
        player1_new_score = player1_current_score + 1
        player2_new_score = player2_current_score
    
    #if player two wins
    elif winner == 2:
        player1_new_score = player1_current_score
        player2_new_score = player2_current_score + 1
    
    #if it is a draw
    else:
        player1_new_score = player1_current_score + 0.5
        player2_new_score = player2_current_score + 0.5

    #new scores for each player after the round
    return player1_new_score, player2_new_score

#function the alows to restart the game
def play_again(decision):

    '''
    Parameters
    ----------
    decision : str

    Returns
    -------
    None.

    '''
    if decision == 'y':
        main()
    else:
        print('--------------------------------------\nThank you for playing, see you next time')

# Calling main function
main()