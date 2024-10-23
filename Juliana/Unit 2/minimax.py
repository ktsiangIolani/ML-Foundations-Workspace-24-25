#bot for minimax tictactoe

def minimaxBot(board, player):
    bestScore, bestMove = recursiveMinimax(board, player)
    board[bestMove[0]][bestMove[1]] = player


def recursiveMinimax(board, player):
    #initialize varibles
    opponent = "X" if player == "O" else "O"
    bestScore = -100 if player == "X" else 100
    bestMove = [None, None]


    # set up base cases
    if check_win(board, "X"):
        return 1, bestMove
    if check_win(board, "O"):
        return -1, bestMove
    if is_board_full(board):
        return 0, bestMove
    
    #setup our recursive case
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                #temporarily placing move at i, j
                board[i][j] = player
                #recursively get the score if we place at i, j
                score = recursiveMinimax(board, opponent)
                #if we are max, update score if it's higher than best score
                if player == "X" and score > bestScore:
                    bestScore = score
                    bestMove = [i,j] #update best move to be this move
                #if we are min, updates score if it's lower than ebst score
                if player == "O" and score < bestScore:
                    bestScore = score
                    bestMove = [i,j] #update best move to be this move
                board[i][j] = " "
    #returns the best score for this board
    return bestScore, bestMove
