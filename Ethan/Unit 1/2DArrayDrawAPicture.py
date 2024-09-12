# Draw a Picture in a 2D Array
# ML Foundations - Ms. Tsiang

# Name: Ethan Mashimo
# Date: 9/10/24

RED = "\033[91m"
RESET = "\033[0m"


def drawPicture(matrix):
    # TODO Given a 10x10 2D array, write a function that draws a 
    # picture of your choice in the array by converting 0s into 'X's

    for i in range(len(matrix)):
        if i == 3 or i == 6:
            matrix[2][i] = 1
        if i >= 2 and i <= 7:
            matrix[4][i] = 1
        if i == 2 or i == 7:
            matrix[5][i] = 1
        if i >= 3 and i <= 6:
            matrix[6][i] = 1
        matrix[0][i] = 1
        matrix[i][0] = 1
        matrix[9][i] = 1
        matrix[i][9] = 1
            

    return matrix

def changeColor(matrix):
    
    for row in matrix:
        for value in row:
            if value == 1:
                print(f"{RED}{value}{RESET}", end=" ")  # Print '1' in red
            else:
                print(value, end=" ")  # Print '0' in default color
        print()  # New line after each row





# initialize a 10x10 2D array with 0s to represent a blank canvas
blankMatrix = [[0 for _ in range(10)] for _ in range(10)]

def main():
    picture = drawPicture(blankMatrix)
    changeColor(picture)  # Call changeColor to display the matrix with color


main()