#start here 

import random

player1_input = input("Player 1: what is your name? ")
player1_number = random.randint(0,100)

player2_input = input("Player2: What is your name? ")
player2_number = random.randint(0,100)

if player2_number > player1_number:
    print(player1_number)
    print(player2_number)
    print( player2_input + " wins")
elif player1_number > player2_number:
    print(player1_number)
    print(player2_number)
    print(player1_input +  " wins")



