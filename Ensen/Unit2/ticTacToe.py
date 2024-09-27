# Machine Learning Foundations 24-25 - Ms. Tsiang
# Tic Tac Toe 

# Name:Ensen Kam
# Date:9/20/24

# Implement a 2 player game of tic tac toe
# Board represents a 3x3 matrix

import random

def playerXTurn(board):
    while True:
        print("Player X")
        row = input("Row: ")
        column = input("Column: ")
        while row not in ["0", "1", "2"]:
            print("Invalid input please try again")
            row = input("Row: ")
        while column not in ["0", "1", "2"]:
            print("Invalid input please try again")
            column = input("Column: ")
        if board[int(row)][int(column)] != " ":
                print("That spot is already taken. Please choose another.")
        else:    
            board[int(row)][int(column)] = "X"
            break

    return board

def playerOTurn(board):
    print("Player O")
    while True:
        row = random.randint(0,2)
        column = random.randint(0,2)
        if board[row][column] == " ":
            board[row][column] = "O"
            break
    return board
        
def check_draw(board):
    #TODO check if the board is full
    #TODO return True if it is, False otherwise
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == " ":
                return False
    return True

def check_winner(board):
    #TODO check if there is a winner
    #TODO return 'X' if 'X' has won, 'O' if 'O' has won, or None if there is no winner
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": # top row
        return "X"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":#middle row
        return "X"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":#bottom row
        return "X"
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":#left column
        return "X"
    elif board[0][1] == "X" and board[1][1] == "X" and board[1][2] == "X":#middle column
        return "X"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":#right column
        return "X"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":#top left to bottom right
        return "X"
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":#top right to bottom left
        return "X"
    
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return "O"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return "O"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "O"
    elif board[0][1] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return "O"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "O"
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "O"
            


# CODE BELOW IS COMPLETE
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)       

def tic_tac_toe():
    board = [[" " for i in range(3)] for i in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        if current_player == 'X':
            playerXTurn(board)
        else:
            playerOTurn(board)
            
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player " + winner + " wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()