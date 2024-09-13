def practice():
    print("Hello, welcome")
practice()

def loop():
    lst = [1, 3, 5, 7, 9]
    for i in lst:
        print(i*2)
loop()

def compare(a,b):
    if a > b:
        return "Greater"
    if a == b:
        return "Equal"
    else:
        return "Smaller"
    
print(compare(5, 3))  # Output: "Greater"
print(compare(2, 2))  # Output: "Equal"
print(compare(1, 4))  # Output: "Smaller"



matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]                  
def array(matrix):
    return matrix[1][2]
print(array(matrix))

def change(matrix):
    matrix[0][0] = 99
    return matrix
print(change(matrix))