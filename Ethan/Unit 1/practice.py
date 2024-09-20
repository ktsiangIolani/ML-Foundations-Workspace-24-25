matrix1 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
matrix2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

#go through the 2D array
# if item is a 1, change to a 0
#ptherwwise change to a 1

# for row i namtrix
#. for column in row
#.   if column is a 1, change to 0
#.   otherwise, change to 1

def flip_matrix(matrix):
    for i in range(len(matrix)): # i represents a row index
        for j in range(len(matrix)): # j represents a column in the ith row
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    print(matrix)

flip_matrix(matrix1)