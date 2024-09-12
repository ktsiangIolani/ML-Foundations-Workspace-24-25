# Draw a Picture in a 2D Array
# ML Foundations - Ms.Tsiang

# Juliana
# 9/10/24

def drawDiagonal(matrix):
    # TODO Given a 10x10 2D array, write a function that draws a picture of your choice in the array by converting 0s into 1s
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 1
        matrix[i][size-1-i] = 1
    return matrix

def drawCross(matrix):
    size = len(matrix)
    middle = size//2
    for i in range(size):
        matrix[middle][i] = 1
        matrix[i][middle] = 1
        matrix[4][i] = 1
        matrix[i][4] = 1   
    return matrix

def color(matrix):
    for row in matrix:
        for value in row:
            if value == 1:
                print("\033[91m1\033[0m", end=" ")
            else:
                print("\033[94m0\033[0m", end=" ")
        print()

#initialize a 10x10 2D array with 0s to represent a blank cnavas
blankMatrix = [[0 for _ in range(10)] for _ in range (10)]

def main():
    picture = drawDiagonal(blankMatrix)
    picture = drawCross(blankMatrix)
    color(picture)

main()