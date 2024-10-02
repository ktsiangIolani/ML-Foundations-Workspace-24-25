# Bot for minimax tic tac toe

def minimaxBot(board, player):
    bestScore, bestMove = recursiveMinimax
    board[bestMove[0]][bestMove[1]] = player

def recursiveMinimax(board, player):
    # initialize variables
    opponent = "X" if player == "O" else "O"
    bestScore = -100 if player == "X" else 100
    bestMove = [None, None]
   
    # setup base cases
    if check_win(board, "X"):
        return 1, bestMove
    if check_win(board, "O"):
        return -1, bestMove
    if is_board_full(board):
        return 0, bestMove
    
    # setup recursive case
    for r in range (len(board)):
        for c in range (len(board[r])): # check each spot
            if board[r][c] == " ": # if the spot is empty
                # temporarily placing a move at spot r, c
                board[r][c] == player 
                # recursively get the score if we place at spot r, c
                score = recursiveMinimax(board, opponent)
                # if we are max, update score if its higher than best score
                if player == "X" and score > bestScore:
                    bestScore = score
                    bestMove = [r, c]
                # if we are min, update score if it's lower than best score
                if player == "O" and score < bestScore:
                    bestScore = score
                    bestMove = [r, c]
                # reset spot r, c back to empty
                board[r][c] == " "
    # returns the best score for this board, this potential move
    return bestScore, bestMove



