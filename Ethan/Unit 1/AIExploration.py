# AI Tool Exploration
# ML Foundations - Ethan Mashimo

#Ethan Masnhimo
#10/9/24

#draws a x in a matrix

matrix = [[0 for i in range(5)] for i in range(5)]

def drawX(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 1

    for i in range(len(matrix)):
        
    
        


def drawO(matrix):
    
    # Ensure n is odd
    if n % 2 == 0:
        raise ValueError("The size of the matrix must be an odd integer.")

    # Create an n x n matrix filled with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Set up the "O" pattern by filling in a single inner layer with 1's
    for i in range(1, n-1):
        matrix[1][i] = 1  # Top row of inner "O"
        matrix[n-2][i] = 1  # Bottom row of inner "O"
        matrix[i][1] = 1  # Left column of inner "O"
        matrix[i][n-2] = 1  # Right column of inner "O"

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

# Example usage
n = 7  # Example odd size
o_matrix = drawO(n)
print_matrix(o_matrix)





def main():
    for row in matrix:
        print(row)
        drawX(matrix)

main()