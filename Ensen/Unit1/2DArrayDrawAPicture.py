# Draw a Picture in a 2D Array
# ML Foundations - Ms. Tsiang

# Name: Ensen 
# Date: 9/10/24

from colorama import Fore, Back, Style

def drawPicture(matrix):
    # TODO Given a 10x10 2D array, write a function that draws a 
    # picture of your choice in the array by converting 0s into 'X's
    for i in (range(10)):
        matrix[8][i] = 1
        matrix[9][i] = 1
    for i in (range(3)):
        matrix[5 + i][5] = 1
        matrix[5 + i][1] = 1
        matrix[5 + i][8] = 1
    for i in (range(4)):
        matrix[4][i + 2 + i] = 1
    matrix[4][0] = 1
    matrix[3][1] = 1
    matrix[3][5] = 1
    matrix[3][7] = 1
    matrix[3][9] = 1
    matrix[2][8] = 1
    return matrix
# initialize a 10x10 2D array with 0s to represent a blank canvas
blankMatrix = [[0 for _ in range(10)] for _ in range(10)]

def main():
    picture = drawPicture(blankMatrix)
    for row in picture:
        for value in row:
            if value == 1:
                print("\033[91m1\033[0m", end = "")
            else:
                print(value, end = "")
        print()
main()