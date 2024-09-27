# Machine Learning Foundations 24-25 - Ms. Tsiang
# Tic Tac Toe 

# Name: Aliya Hamdani
# Date: 9/20/24

# Implement a 2 player game of tic tac toe
# Board represents a 3x3 matrix

def playerXTurn(board):
    #TODO ask the player for an input row and column
    #TODO check if it's a valid move. If it isn't ask them to try again
    #TODO update the board with an X
    # Checks if user's row and column are in the board's range
    rowPos = int(input("Enter the row number you want to place an X in: "))
    while rowPos > 2 or rowPos < 0:
        rowPos = int(input("Invalid row number. Enter 0, 1, or 2 for the row number you want to place an X in: "))
    colPos = int(input("Enter the column number you want to place an X in: "))
    while colPos > 2 or colPos < 0:
        colPos = int(input("Invalid column number. Enter 0, 1, or 2 for the column number you want to place an X in: "))
    # Checks that the user's position is empty
    while board[rowPos][colPos] != " ":
        print("Invalid. This space has already been filled. Please enter a new position.")
        rowPos = int(input("Enter the row number you want to place an X in: "))
        colPos = int(input("Enter the column number you want to place an X in: "))
    board[rowPos][colPos] = 'X' # Updates board with X in user's position
    

def twoAsNoBs(list, a, b): # returns True if there are two X's in a given list and no O's
    count = 0
    for item in list:
        if item == a:
            count += 1
        elif item == b:
            count -= 1
    if count == 2:
        return True


def mustFill(board): # returns True if X or O is about to win, and the row and column index to fill; false if otherwise
    result_check_rows = check_rows(board); result_check_columns = check_columns(board); result_check_diagonals = check_diagonals(board)
    
    if result_check_rows is not None:
        if result_check_rows[0] == 'fill':
            r = result_check_rows[1]
            c = board[r].index(" ")
            return True, r, c
    elif result_check_columns is not None:
        if result_check_columns[0] == 'fill':
            r = result_check_columns[1]
            c = result_check_columns[2]
            return True, r, c
    elif result_check_diagonals is not None:
        if result_check_diagonals[0] == 'fill':
            return True, result_check_diagonals[1], result_check_diagonals[2]
    else:
        return False, int, int
    

def playerOTurn(board, round):
    #TODO ask the player for an input row and column
    #TODO check if it's a valid move. If it isn't ask them to try again
    #TODO update the board with an O
    # Checks if user's row and column are in the board's range
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    result_mustFill = mustFill(board)
    moved = False
    if result_mustFill[0] is False:
        if round == 1:
            if board[1][1] == " ": # first choice is centre, second choice: top left corner if X took centre
                board[1][1] = 'O'; moved = True
            else:
                board[0][0] = 'O'; moved = True
        if round > 1:
            for corner in corners: # take corners first
                if board[corner[0]][corner[1]] == " ":
                    board[corner[0]][corner[1]] = "O"
                    moved = True
                    break
            if moved is False:
                for r in range(len(board)):
                    for c in range(len(board[r])): # if all corners filled, just take first available space
                        if board[r][c] == " ":
                            board[r][c] = "O"
                            moved = True
                            break
    elif mustFill(board)[0] == True:
        board[result_mustFill[1]][result_mustFill[2]] = 'O'


def check_draw(board):
    #TODO check if the board is full
    #TODO return True if it is, False otherwise
    count = 0
    for r in range(len(board)): # Goes through each row adding 1 to count if there are no empty spaces
        if " " not in board[r]:
            count += 1
    if count == len(board): # If all of the rows have no empty spaces, then board is full
        return True
    else:
        return False
    

def check_rows(board):
    for rowNum in range(len(board)):
        if board[rowNum] == ['X', 'X', 'X']:
            return 'X'
        elif board[rowNum] == ['O', 'O', 'O']:
            return 'O'
        elif twoAsNoBs(board[rowNum], 'X', 'O') or twoAsNoBs(board[rowNum], 'O', 'X'): # for mustFill()
            return ('fill', rowNum)
        
        
def check_columns(board):
    for col in range(len(board)):
        column = []
        for row in range(len(board)):
            column.append(board[row][col])
        if column == ['X', 'X', 'X']:
            return 'X'
        elif column == ['O', 'O', 'O']:
            return 'O'
        elif twoAsNoBs(column, 'X', 'O') or twoAsNoBs(column, 'O', 'X'): # for mustFill()
            return ('fill', column.index(" "), col)
        

def check_diagonals(board):
    leftToRightDiagonal = []
    rightToLeftDiagonal = []
    for i in range(len(board)):
        leftToRightDiagonal.append(board[i][i])
        rightToLeftDiagonal.append(board[i][2 - i])
    if leftToRightDiagonal == ['X', 'X', 'X'] or rightToLeftDiagonal == ['X', 'X', 'X']:
        return 'X'
    elif leftToRightDiagonal == ['O', 'O', 'O'] or rightToLeftDiagonal == ['O', 'O', 'O']:
        return 'O'
    # for mustFill()
    if twoAsNoBs(leftToRightDiagonal, 'X', 'O') or twoAsNoBs(leftToRightDiagonal, 'O', 'X'):
        return ('fill', leftToRightDiagonal.index(" "), leftToRightDiagonal.index(" "))
    if twoAsNoBs(rightToLeftDiagonal, 'X', 'O')or twoAsNoBs(rightToLeftDiagonal, 'O', 'X'):
        return ('fill', rightToLeftDiagonal.index(" "), 2 - rightToLeftDiagonal.index(" "))
    

def check_winner(board):
    #TODO check if there is a winner
    #TODO return 'X' if 'X' has won, 'O' if 'O' has won, or None if there is no winner
    if check_rows(board) == 'X':
        return 'X'
    elif check_rows(board) == 'O':
        return 'O'

    if check_columns(board) == 'X':
        return 'X'
    elif check_columns(board) == 'O':
        return 'O'
    
    if check_diagonals(board) == 'X':
        return 'X'
    elif check_diagonals(board) == 'O':
        return 'O'
    
    return None


# CODE BELOW IS COMPLETE
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)       

def tic_tac_toe():
    board = [[" " for i in range(3)] for i in range(3)]
    current_player = "X"
    round = 1

    while True:
        print_board(board)
        if current_player == 'X':
            playerXTurn(board)    
        else:
            playerOTurn(board, round)
            round +=1
            
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