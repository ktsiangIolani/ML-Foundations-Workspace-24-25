# Draw a Picture in a 2D Array
# ML Foundations - Ms. Tsiang
###TESTING
# Name: Aliya
# Date: 09/10/24

# Function to make number green
def makeGreen(number):
    green = "\033[92m" # ANSI escape sequence for green colour
    reset = "\033[0m"  # Reset to default colour
    
    # Return the number in green and rest colour so next number is not green
    return f"{green}{number}{reset}"

# Function to change values in a row to 1; inputs: row number, index to start from, how many values to change
def changeRow(matrix, rowIndex, startIndex, total):
    for i in range(total):
        matrix[rowIndex][startIndex] = 1
        startIndex += 1

# Function to change values in a column to 1; inputs: column number, index to start from, how many values to change
def changeColumn(matrix, columnIndex, startIndex, total):
    for i in range(total):
        matrix[startIndex][columnIndex] = 1
        startIndex += 1
    
# Function to draw a spiral by modifying the matrix values
def drawPicture(matrix):

    length = len(matrix) # Accounts for a matrix of any even square size
    indent = 0 
    total = length
    lineNum = 0
    for i in range(length): #fills top row
        matrix[0][i] = 1
    while indent < (length/2):
        changeColumn(matrix, lineNum, indent, total) #first column 10 indented 0 ## 2nd column 6 indented 2 ### 4th column 2 indented 4
        changeRow(matrix, length - 1 - lineNum, indent, total) #last row 10 indented 0 ## 2nd to last row 6 indented 2 ### 5th column 2 indented 4
        indent += 2 # 2 ## 4 ## 6 and stops
        total -= 2 # 8 ## 4
        changeColumn(matrix, length - 1 - lineNum, indent, total) #last column 8 indented 0 ## 2nd to last column 4 indented 4
        lineNum += 2 #2 # 4
        changeRow(matrix, lineNum, indent, total) # first 2nd row 8 indented 2 ## 3rd row 4 indented 4
        total -= 2 # 6 ## 2
    return matrix

# initialize a 10x10 2D array with 0s to represent a blank canvas
blankMatrix = [[0 for _ in range(10)] for _ in range(10)]

def printMatrix(matrix):
    for row in matrix:
        # Loop through each element in the row
        for element in row:
            # If the element is 1, make it green
            if element == 1:
                print(makeGreen(element), end=' ')  # Print green number with space at end instead of a new line
            else:
                print(element, end=' ')  # Print 0s non-coloured with space at end instead of a new line
        print()  # Newline after each row

def main():
    picture = drawPicture(blankMatrix) # Calls drawPicture to put spiral shape into the matrix
    printMatrix(picture)  # Calls printMatrix to display with colours
    
main()














###TRASH
'''
def drawPicture(matrix):
    for i in range(10):
        matrix[0][i] = 1   # Top border
        matrix[i][0] = 1   # Left border
        matrix[9][i] = 1   # Bottom border
        if i > 1:
            matrix[i][9] = 1   # Right edge
        if i > 1:
            matrix[2][i] = 1   # Horizontal line

    for i in range(8):
        if i > 2:
            matrix[i][2] = 1   # Vertical line on the left
        if i > 2:
            matrix[7][i] = 1   # Horizontal line near the bottom
        
    for i in range(7):
        if i > 3:
            matrix[i][7] = 1   # Vertical line on the right
        if i > 3:
            matrix[4][i] = 1   # Horizontal line in the middle
        
    for i in range(6):
        if i > 3:
            matrix[5][i] = 1   # Horizontal line near the middle
'''