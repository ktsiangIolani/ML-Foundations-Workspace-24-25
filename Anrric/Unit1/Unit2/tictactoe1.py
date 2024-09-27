# Machine Learning Foundations 24-25 - Ms. Tsiang
# Tic Tac Toe 
import random
# Name:Anrric Xu
# Date:9/20/24

# Implement a 2 player game of tic tac toe
# Board represents a 3x3 matrix
def playerOTurn(board):
    while True:
        user_row = int(input(" player O: what row would you like to use? "))
        user_column = int(input("player O: what column would you like to use? "))
        
        if (0 <= user_row < 3) and (0 <= user_column < 3) and (board[user_row][user_column] == " "):
            board[user_row][user_column] = "O"
            return board[user_row][user_column]
            break
        else:
            print("Invalid input. Please try again.")

def playerXTurn(board):
    while True:
        user_row = int(input("player X: what row  would you like to use? "))
        user_column = int(input("player X: what column (0-2) would you like to use? "))
        
        if (0 <= user_row < 3) and (0 <= user_column < 3) and (board[user_row][user_column] == " "):
            board[user_row][user_column] = "X"
            break
        else:
            print("Invalid input. Please try again.")
    
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None
def bot_player(board):
    random_row = random.randrange(0,2)
    random_col = random.randrange(0,2)
    while True:
     if (0 <= random_row < 3) and (0 <= random_col < 3) and (board[random_row][random_col] == " "):
            board[random_row][random_col] = "O"
            break
     else: 
        random_row = random.randrange(0,3)
        random_col = random.randrange(0,3)
        if (0 <= random_row < 3) and (0 <= random_col < 3) and (board[random_row][random_col] == " "):
            board[random_row][random_col] = "O"
            break


    

    



         

# CODE BELOW IS COMPLETE
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)       

def tic_tac_toe():
    turn_count = 0
    board = [[" " for i in range(3)] for i in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print("")
        if current_player == 'X':
            turn_count += 1
            playerXTurn(board)
            print(turn_count)
        else:
            turn_count += 1
            bot_player(board)
            print(turn_count)
            
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