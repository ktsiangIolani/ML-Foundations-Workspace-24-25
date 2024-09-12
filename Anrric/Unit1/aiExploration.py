#AI Tool Exploration
#ML Foundation -Ms.Tsiang

#anrric xu
#9/9/24

#Draw a X in a matrix
fivebyfive = [[0 for i in range(5)] for i in range(5)]
def drawX(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 1
    pass


def drawO(matrix):
    middle = len(matrix) // 2
    for i in matrix[middle]:
        matrix[0][i] = 1
        
        
                   
                   


    pass






def main():
    drawX(fivebyfive)
    for row in fivebyfive:
        
        print(row)
    oShape = drawO(fivebyfive)
    pass
main()