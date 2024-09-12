# AI Tool Exploration
# ML Foundations
# Juliana Shi
# September 9

# Draws a x in a matrix

matrix = [[0 for i in range(5)] for i in range(5)]
matrix2 = [[0 for i in range(5)] for i in range(5)]


def drawX(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 1               
        matrix[i][size - i - 1] = 1         
drawX(matrix)

def drawO(matrix2):
    for row in range(4):
        matrix2[1][row+1] = 1
        matrix2[row+1][1] = 1
        matrix2[3][row+1] = 1
        matrix2[row+1][3] = 1
        matrix2[1][4] = 0
        matrix2[3][4] = 0
        matrix2[4][1] = 0
        matrix2[4][3] = 0
drawO(matrix2)


def main():
    for row in matrix:
        print(row)
    print("")
    for row in matrix2:
        print(row)
    pass

main()