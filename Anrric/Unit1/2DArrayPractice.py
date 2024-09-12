# ML Foundations
# 2D Array Practice - Ms. Tsiang
# Name: AnrricXu
# Date: 9/7/24

#TODO: Write a function to find the center element of a 2D array
# Assume that there will be a center element
def find_center(matrix):
    center_length = len(matrix) // 2
    center_width = len(matrix[0]) // 2
    return matrix[center_length][center_width]
pass

#TODO: Write a function to print the diagonal of a 2D array in the format [a, b, c]
def print_diagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    return diagonal

pass

# TODO: Write a function to calculate the sum some row, 
# where matrix is a 2D array and row is an integer representing a row in the 2D array
def sum_of_row(matrix, row):
    row_sum = sum(matrix[row])
    return row_sum
pass

# TODO: Write a function to calculate the sum some column, 
# where matrix is a 2D array and row is an integer representing a row in the 2D array
def sum_of_column(matrix, column):
    column_sum = 0
    for row in matrix:
        column_sum = column_sum + row[column]
    return column_sum
pass

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
