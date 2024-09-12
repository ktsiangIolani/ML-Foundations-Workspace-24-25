#AI Tool Exploration
#Name: Aliya Hamdani
#Date: 09/09/24


fivebyfive = [[0 for i in range(5)] for i in range(5)]

#Draws a x in a matrix
def drawX(matrix):
    pass



def drawO(matrix):
    for r in range(len(matrix)):
        if r == 1 or r == (len(matrix) - 2):
            for c in range(len(matrix) - 1):
                if c != 0:
                    matrix[r][c] = 1
        elif r != 0 and r != (len(matrix) - 1):
            matrix[r][1] = 1
            matrix[r][len(matrix) - 2] = 1
    for row in fivebyfive:
        print(row)



def main():
    '''for row in fivebyfive:
        print(row)'''
    drawO(fivebyfive)
main()