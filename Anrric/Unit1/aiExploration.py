# AI Tool Exploration
# ML Foundation - Ms. Tsiang

# anrric xu
# 9/9/24

def create_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def drawX(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 1
        matrix[i][size - i - 1] = 1

def drawO(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[0][i] = 1
        matrix[size - 1][i] = 1

    for i in range(1, size - 1):
        matrix[i][0] = 1
        matrix[i][size - 1] = 1


def printMatrix(matrix):
    for row in matrix:
        print(row)

def main():
    size = 5
    
    # Create and draw X on matrix
    matrix_x = create_matrix(size)
    drawX(matrix_x)
    print("Matrix with X:")
    printMatrix(matrix_x)

    # Create and draw O on matrix
    matrix_o = create_matrix(size)
    drawO(matrix_o)
    print("Matrix with O:")
    printMatrix(matrix_o)

if __name__ == "__main__":
    main()
