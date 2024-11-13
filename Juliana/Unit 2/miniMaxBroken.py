# Minimax algorith
from math import inf

# ---------------------------  BROKEN CODE FOR MINIMAX ALGORITHM (FIX 5 THINGS!) ----------------------------

def recursiveMinimax(board, player):
    #initialize variables
    bestScore = -inf if player == "X" else inf
    opponent = "X" if player == "O" else "O"
    bestMove = [None, None]

    #setup base case with rewards
    if check_win(board, "X"):
        return 1, bestMove 
    if check_win(board, "O"):
        return -1, bestMove
    if is_board_full(board):
        return 0, bestMove
    
    # setup recursive case
    # check all possible spots and calculate the max/min score recurisively
    for i in range(len(board)):
        for j in range(len(board)): 
            if board[i][j] == " ":
                #place move temporarily
                board[i][j] = player
                score, _ = recursiveMinimax(board, opponent) 
                if player == "X" and score > bestScore:
                    bestScore = score
                    bestMove = [i, j]
                elif player == "O" and score < bestScore:
                    bestScore = score
                    bestMove = [i, j]
                #once score is calculated remove piece
                board[i][j] = " "
    return bestScore, bestMove


# --------------------------- WORKING CODE FOR TIC TAC TOE ---------------------------

def minimax_bot_move(board, player):
    print("Minimax Bot Turn")
    bestScore, bestMove = recursiveMinimax(board, player)
    if bestMove[0] != None:
        board[bestMove[0]][bestMove[1]] = player

#random bot move
def random_bot_move(board, player):
    while True:
        print("Your Turn")
        row = int(input("Enter a row: "))
        col = int(input("Enter a col: "))
        #check if move is valid
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
            break
        
# Check for a win condition
def check_win(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full (i.e., a tie)
def is_board_full(board):
    return all([spot != ' ' for row in board for spot in row])

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
            random_bot_move(board, 'X')
        else:
            minimax_bot_move(board, 'O')
            
        if check_win(board, 'X'):
            print("X wins")
            break
        if check_win(board, 'O'):
                print("O wins")
                break
        if is_board_full(board):
            print("It's a tie!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()