# Machine Learning Foundations 24-25 - Ms. Tsiang
# Tic Tac Toe 

# Name: Juliana Shi
# Date: 9/20/2024

# Implement a 2 player game of tic tac toe
# Board represents a 3x3 matrix

def playerXTurn(board):
    #Input of player X
    while True:
        user_answer = input("Input row and column in the format: [i,j]")
        if user_answer in ["[0,0]", "[0,1]", "[0,2]", "[1,0]", "[1,1]", "[1,2]", "[2,0]", "[2,1]", "[2,2]"]:
            row = int(user_answer[1])
            column = int(user_answer[3])
            if board[row][column] == " ":
                board[row][column] = 'X'
                break
            else:
                print("Invalid move, cell already taken.")
        else:
            print("Invalid input format. Please use [i,j].")

def playerOTurn(board):
    #Bot strategy to winning
    if blockMove(board): # blocks winning move of player X
        return
    if board[1][1] == " ": #takes center spot if available
        board[1][1] = 'O'
        return
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)] #takes corner
    for i in corners:
        if board[i[0]][i[1]] == " ":
            board[i[0]][i[1]] = "O"
            return
    for i in range(len(board)): #takes any spot if no other move is found
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = "O"
                return

def blockMove(board):
    # Check rows for winning moves
    for i in range(3):
        if board[i].count("X") == 2 and board[i].count(" ") == 1:
            board[i][board[i].index(" ")] = 'O'
            return True
            
    # Check columns for winning moves
    for i in range(3):
        column = [board[0][i], board[1][i], board[2][i]]
        if column.count("X") == 2 and column.count(" ") == 1:
            board[column.index(" ")][i] = 'O'
            return True
            
    # Check diagonals forwinning moves
    if board[0][0] == board[1][1] == "X" and board[2][2] == " ":
        board[2][2] = "O"
        return True
    if board[0][2] == board[1][1] == "X" and board[2][0] == " ":
        board[2][0] = "O"
        return True

    # Block the center if X occupies the corners
    if board[0][0] == "X" and board[2][2] == "X" and board[1][1] == " ":
        board[1][1] = "O"
        return True
    if board[0][2] == "X" and board[2][0] == "X" and board[1][1] == " ":
        board[1][1] = "O"
        return True
    
    return False

def check_draw(board):
    #checks if the board is full meaning it is a tie
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                return False
    return True

def check_winner(board):
    #checks the winner 
    for i in range(3):
        #checks rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        #checks columns
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    #checks diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    #checks diagonals
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  
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

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()