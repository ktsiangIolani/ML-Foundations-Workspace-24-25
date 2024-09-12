#initialize a 3x3 matrix
matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#set the center element to 1
matrix[1][1] = 1
matrix[1][0] = 1
matrix[1][2] = 1

for i in range(len(matrix)):
    matrix[1][i] = 1

matrix[1] = [1,1,1]

for row in matrix:
    print(row)


