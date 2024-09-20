# ML Foundations
# 2D Array Traversal Practice - Ms. Tsiang
# Name: Ethan Mashimo
# Date: 


# Given an nxm matrix, multiply each item by 2. 
def double_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j] * 2
    return matrix

# TODO:Given an nxm matrix, replace all instances of the number 5 with the number 2.
def replace_num(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 5:
                matrix[i][j] = 2
    return matrix


# ------ TEST CASES: DO NOT MODIFY THE CODE BELOW! --------
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def test(function, input, expected_output):
    output = function(input)
    did_pass = output == expected_output
    color = bcolors.OKGREEN if did_pass else bcolors.FAIL
    if did_pass:
        print(color + "Test Passed" + bcolors.ENDC)
    else:
        print(color + "Test Failed" + bcolors.ENDC)
        print(color + "Input: " + str(input) + " Expected Output: " + str(expected_output) + " Output: " + str(output) + bcolors.ENDC)
# Test cases
if __name__ == "__main__":
    # Test case 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 5],
        [7, 8, 9]
    ]
    
    print("Matrix 1:")
    for row in matrix1:
        print(row)
    
    test(double_matrix, matrix1, [
        [2, 4, 6],
        [8, 10, 10],
        [14, 16, 18]
    ])
    matrix1 = [
        [1, 2, 3],
        [4, 5, 5],
        [7, 8, 9]
    ]
    test(replace_num, matrix1,  [
        [1, 2, 3],
        [4, 2, 2],
        [7, 8, 9]
    ])


    # Test case 2
    matrix2 = [
        [3, 8, 5],
        [7, 5, 4],
        [5, 9, 6]
    ]
    
    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    test(double_matrix, matrix2, [
        [6, 16, 10],
        [14, 10, 8],
        [10, 18, 12]
    ])
    matrix2 = [
        [3, 8, 5],
        [7, 5, 4],
        [5, 9, 6]
    ]

    test(replace_num, matrix2, [
        [3, 8, 2],
        [7, 2, 4],
        [2, 9, 6]
    ])
    print("Test case 2 passed.")