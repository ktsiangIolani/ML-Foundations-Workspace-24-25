# Draw a Picture in a 2D Array
# ML Foundations - Ms. Tsiang

# Name: Anrric Xu
# Date: 9/10/24

def drawPicture(matrix):
    # TODO Given a 10x10 2D array, write a function that draws a 
    # picture of your choice in the array by converting 0s into 'X's
    for i in range(2,5):
        for j in range(5 - i, 5 + i):
            matrix[i][j] = 'X'
    for i in range(5,9):
        for j in range(2,8):
            matrix[i][j] = 'X'
    for i in range(7,9):
        for j in range(4,6):
            matrix[i][j] = '0'


    return matrix





# initialize a 10x10 2D array with 0s to represent a blank canvas
blankMatrix = [[0 for _ in range(10)] for _ in range(10)]

def main():
    picture = drawPicture(blankMatrix)
    for row in picture:
        print(row)
main()