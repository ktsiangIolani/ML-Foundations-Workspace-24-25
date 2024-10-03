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
    board[rowPos][colPos] = 'X'
    pass

'''def checkSurroundings(tempBoard, row, col):
    count = 0
    #bottom
    if row < 2: 
        bottomExists = True
        if tempBoard[row+1][col] == 'O':
            count += 1
    else:
        bottomExists = False
    #top
    if row > 0:
        topExists = True
        if tempBoard[row-1][col] == 'O':
            count += 1
    else:
        topExists = False
    #right side
    if col < 2:
        if tempBoard[row][col+1] == 'O': #right
            count += 1
        if bottomExists:
            if tempBoard[row+1][col+1] == 'O': #bottom right
                count += 1
        if topExists:
            if tempBoard[row-1][col+1] == 'O': #top right
                count += 1
    #left side
    if col > 0:
        if tempBoard[row][col-1] == 'O': #left
            count += 1
        if bottomExists:
            if tempBoard[row+1][col-1] == 'O': #bottom left
                count += 1
        if topExists:
            if tempBoard[row-1][col-1] == 'O': #top left
                count += 1
    return count'''

'''def copy(board):
    copy = []
    for r in range(len(board)):
        new_row = []  # Create a new row list
        for c in range(len(board[r])):
            new_row.append(board[r][c])  # Append each element to the new row
        copy.append(new_row)  # Append the new row to the board
    return copy'''

def playerOTurn(board):
    #TODO ask the player for an input row and column
    #TODO check if it's a valid move. If it isn't ask them to try again
    #TODO update the board with an O
    # Checks if user's row and column are in the board's range
    rowPos = int(input("Enter the row number you want to place an O in: "))
    while rowPos > 2 or rowPos < 0:
        rowPos = int(input("Invalid row number. Enter 0, 1, or 2 for the row number you want to place an O in: "))
    colPos = int(input("Enter the column number you want to place an O in: "))
    while colPos > 2 or colPos < 0:
        colPos = int(input("Invalid column number. Enter 0, 1, or 2 for the column number you want to place an O in: "))
    # Checks that the user's position is empty
    while board[rowPos][colPos] != " ":
        print("Invalid. This space has already been filled. Please enter a new position.")
        rowPos = int(input("Enter the row number you want to place an O in: "))
        colPos = int(input("Enter the column number you want to place an O in: "))
    board[rowPos][colPos] = 'O' 

    '''indexesOScores = []
    Oscores = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            temp = copy(board)
            if board[r][c] == " ":
                temp[r][c] = 'O'
                if check_winner(temp) == 'O':
                    print("win")
                    board[r][c] = 'O'
                    pass
                indexesOScores.append([r, c])
                Oscores.append(checkSurroundings(temp, r, c))
    bestMove = indexesOScores[Oscores.index(max(Oscores))]
    board[bestMove[0]][bestMove[1]] = 'O'
    '''

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
    for row in range(len(board)):
        if board[row] == ['X', 'X', 'X']:
            return 'X'
        elif board[row] == ['O', 'O', 'O']:
            return 'O'
        
def check_columns(board):
    for col in range(len(board[0])):
        column = []
        for row in range(len(board)):
            column.append(board[row][col])
        if column == ['X', 'X', 'X']:
            return 'X'
        elif column == ['O', 'O', 'O']:
            return 'O'

def check_diagonals(board):
    leftToRightDiagonal = []
    rightToLeftDiagonal = []
    for i in range(len(board)):
        leftToRightDiagonal.append(board[i][i])
        rightToLeftDiagonal.append(board[i][len(board[i]) - 1 - i])
    if leftToRightDiagonal == ['X', 'X', 'X'] or rightToLeftDiagonal == ['X', 'X', 'X']:
        return 'X'
    elif leftToRightDiagonal == ['O', 'O', 'O'] or rightToLeftDiagonal == ['O', 'O', 'O']:
        return 'O'

def check_winner(board):
    #TODO check if there is a winner
    #TODO return 'X' if 'X' has won, 'O' if 'O' has won, or None if there is no winner
    # Checks rows
    if check_rows(board) == 'X':
        return 'X'
    elif check_rows(board) == 'O':
        return 'O'

    # Checks columns 
    if check_columns(board) == 'X':
        return 'X'
    elif check_columns == 'O':
        return 'O'
    
    # Checks diagonals
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


