# ML Foundations
# 2D Array Practice - Ms. Tsiang
# Name: Ethan Mashimo
# Date:

#TODO: Write a function to find the center element of a 2D array
# Assume that there will be a center element
def find_center(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    centerRow = rows // 2
    centerColumn = columns // 2
    print("center:", matrix[centerRow][centerColumn])
    return matrix[centerRow][centerColumn]
    
#TODO: Write a function to print the diagonal of a 2D array in the format [a, b, c]
def print_diagonal(matrix):
    diagonalElements = [matrix[i][i] for i in range(len(matrix))]
    print("elements in diagonal:", diagonalElements)
# TODO: Write a function to calculate the sum some row, 
# where matrix is a 2D array and row is an integer representing a row in the 2D array
def sum_of_row(matrix, row):
    total = 0
    for element in matrix[row]: 
        total += element
    print ("Row:", total)
    return total


# TODO: Write a function to calculate the sum some column, 
# where matrix is a 2D array and row is an integer representing a row in the 2D array
def sum_of_column(matrix, column):
    total = 0
    for element in matrix:
        total += element[column]
    print ("Column:", total)
    return total

# Test cases
if __name__ == "__main__":
    # Test case 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matrix 1:")
    for row in matrix1:
        print(row)
    
    assert find_center(matrix1) == 5
    print_diagonal(matrix1)
    assert sum_of_row(matrix1, 0) == 6
    assert sum_of_row(matrix1, 1) == 15
    assert sum_of_column(matrix1, 0) == 12
    assert sum_of_column(matrix1, 1) == 15
    print("Test case 1 passed.")

    # Test case 2
    matrix2 = [
        [3, 8, 1],
        [7, 2, 4],
        [5, 9, 6]
    ]
    
    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    assert find_center(matrix2) == 2
    print_diagonal(matrix2)
    assert sum_of_row(matrix2, 0) == 12
    assert sum_of_row(matrix2, 1) == 13
    assert sum_of_column(matrix2, 0) == 15
    assert sum_of_column(matrix2, 2) == 11
    print("Test case 2 passed.")