#bot for minimax tic tac toe

def minimax_bot(board,player):
    best_score, best_move = recursive_minimax(board,player)
    board[best_move[0],best_move[1]] = player 
def recursive_minimax(board,player):
    #initialize some variables 
    opponent = "X" if player == "O" else "O"
    best_score = -100 if player == "X" else 100
    best_move = [None,None]

    #set up base cases 
    if check_win(board,"X"):
        return 1, best_move
    if check_win(board,"O"):
        return -1, best_move
    if is_board_full(board):
        return 0, best_move
    
    #setup our recursive case 
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                #temporarily placing moves at i,j
                board[i][j] = player 
                #recursively get the score at i,j 
                score = recursive_minimax(board, opponent)
                #if we are max then update score if its higher than the score
                if player == "X" and score > best_score:
                    best_score = score
                    best_move = [i,j] #updates the best move to this move 
                #if we are min then update score if its lower than the score
                if player == "O" and score < best_score:
                    best_score = score 
                    best_move = [i,j] #updates the best move to this move 
                board[i][j] = " "
    #returns the best score for this board
    return best_score, best_move







    
