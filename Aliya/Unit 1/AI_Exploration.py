#AI Tool Exploration
#Name: Aliya Hamdani
#Date: 09/09/24




#Draws a x in a matrix
def drawX(matrix):
    length = len(matrix)
    # Fill the matrix to draw an "X"
    for i in range(length):
        matrix[i][i] = 1            # Primary diagonal
        matrix[i][length - i - 1] = 1    # Anti-diagonal
    
    # Print the matrix row by row
    for row in matrix:
        print(row)



def drawO(matrix):
    for r in range(len(matrix)):
        if r == 1 or r == (len(matrix) - 2):
            for c in range(len(matrix) - 1):
                if c != 0:
                    matrix[r][c] = 1
        elif r != 0 and r != (len(matrix) - 1):
            matrix[r][1] = 1
            matrix[r][len(matrix) - 2] = 1
    for row in matrix:
        print(row)



def main():
    '''for row in fivebyfive:
        print(row)'''
    fivebyfive = [[0 for i in range(5)] for i in range(5)]
    drawO(fivebyfive)
    print()
    fivebyfive = [[0 for i in range(5)] for i in range(5)]
    drawX(fivebyfive)
main()