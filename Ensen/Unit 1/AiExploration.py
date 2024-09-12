# AI Tool Exploration
# ML Foundations - Ms. Tsiang

#Ensen Kam
#9/9/24

matrix = [[0 for i in range(5)] for i in range(5)]
#Draws a x in a matrix
def drawX(matrix):
    size = len(matrix)
    for i in range(len(matrix)):
        matrix[i][i] = 1
    print(matrix)



def create_circle_matrix(n):
    # Initialize an n x n matrix filled with 0's
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Determine the center of the matrix
    center = n // 2
    
    # Draw a circle in the next layer from the outermost edge
    for i in range(n):
        for j in range(n):
            # Calculate the distance from the center
            dist = ((i - center) ** 2 + (j - center) ** 2) ** 0.5
            
            # If the distance is approximately within one layer inside the outer edge, set it to 1
            if center - 1 <= dist < center:
                matrix[i][j] = 1
    
    return matrix

def main():
    n = 7  # Matrix size (should be odd for symmetry)
    circle_matrix = create_circle_matrix(n)
    for row in circle_matrix:
        print(row)
    drawX(matrix)
main()