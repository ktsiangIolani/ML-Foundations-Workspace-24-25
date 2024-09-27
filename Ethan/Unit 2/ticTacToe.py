# Machine Learning Foundations 24-25 - Ms. Tsiang
# Tic Tac Toe 

# Name: Ethan
# Date:

# Implement a 2 player game of tic tac toe
# Board represents a 3x3 matrix

import random

def playerXTurn(board):
    #TODO ask the player for an input row and column
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    #TODO check if it's a valid move. If it isn't ask them to try again
    if row != len(board) and row >= 4 and column != len(board) and column >= 4:
        print("try again")
    #TODO update the board with an X
    board[row][column] = 'x'
    

def playerOTurn(board):
    #TODO ask the player for an input row and column
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                board[i][j] = "o"
                if check_winner(board) == 'o':  
                    return  
                board[i][j] = " "
     # block opponent's winning move
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                board[i][j] = 'x'  
                if check_winner(board) == 'x':
                    board[i][j] = 'o'  
                    return
                board[i][j] = " "  
     
    if board[1][1] == " ":
        board[1][1] = 'o'
        return
    
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for row, col in corners:
        if board[row][col] == " ":
            board[row][col] = 'o'
            return
        
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for row, col in edges:
        if board[row][col] == " ":
            board[row][col] = 'o'
            return
    

def check_draw(board):
    #TODO check if the board is full
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return False
    return True
    #TODO return True if it is, False otherwise
    

def check_winner(board):
    #TODO check if there is a winner
    for i in range(len(board)): # check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    for j in range(len(board)): #check columns
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]
        
    if board[0][0] == board[1][1] == board[2][2] != " ": #check diagonals
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
        

    #TODO return 'X' if 'X' has won, 'O' if 'O' has won, or None if there is no winner
    return None


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