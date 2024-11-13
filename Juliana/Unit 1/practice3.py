# Unit Test 1
# ML Foundations Period 2 Ms. Tsiang

# Name:
# Date:

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
"""
PART 1 GENERAL PYTHON PROGRAMMING
"""
# Question 1: ( 2 points ) Print Hello <name> 
# for example, if name is "Alice", the function should print "Hello Alice"
def print_hello(name):
    print("Hello", name)

# Question 2: ( 2 points ) Given a nonempy string s, count the number of vowels in the list 
def number_vowels(s):
    count = 0
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            count = count +1
    return count


# Question 3: ( 4 points ) Given a nonempty list of numbers, return the number that is cloest to zero 
# If there are two numbers equally close to zero, return the larger one
# You may NOT use the built in abs function, however you may write your own abs function.
def find_closest_to_zero(numbers):
    closest = numbers[0]
    for num in numbers:
        abs = num
        if num < 0:
            num = 0 - num
        if num < closest:
            closest = abs
    return closest


            


"""
PART 2 MATRIX MANIPULATION
"""
# Question 4: ( 2 points ) Given a nxn matrix with at least 2 rows and 2 columns, return the sum of the corners of the matrix 
def sum_corners(matrix):
    sum = 0
    size = (len(matrix)-1)
    for i in range(size):
        sum = matrix[0][size] + matrix[size][0] + matrix[0][0] + matrix[size][size]
    return sum


# Question 5: ( 4 points ) Given a nxm matrix, change each 0 to a 1 and each 1 to a 0 
def flip_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix



# Question 6: ( 4 points ) Given an nxn (where n is odd) square matrix filled with 0s that has at least 3 rows and at least 3 columns, 
# return a matrix with a z drawn in the matrix by turning 0s to 1s in a Z pattern 
def drawZ(matrix):
    size = len(matrix)
    for i in range(len(matrix)):
        matrix[0][i] = 1
        matrix[size-1][i] = 1
        matrix[i][size - i -1] = 1
    return matrix



"""
PART 3 COSINE SIMILARITY
"""

# Question 7: ( 2 points ) Using the function calculateCosineSimilarity, write a function answerQuestion that 
# answers the user's question if there is a cosine similarity of at least 0.5 
# between the user's question and the question "How far away is the moon?" 

# Given two strings, this function calculates the cosine similarity between the two strings
def calulateConsineSimilarity(string1, string2):
    #create the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    # Vectorize the questions
    tfidf_matrix = vectorizer.fit_transform([string1, string2])
    # Calculate the cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

question = "How far away is the moon?"
answer = "238,855 miles"

#TODO fill out this function. 
# Return answer if the question is with .5 cosine similarity of the question.
# Return -1 otherwise.
def answerQuestion(userQuestion):
    similarity = calulateConsineSimilarity(userQuestion, question)
    if similarity >= .5:
        return answer
    return -1






# ------ TEST CASES: DO NOT MODIFY THE CODE BELOW! --------
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def test(function, input, expected_output):
    did_pass = function(input) == expected_output
    color = bcolors.OKGREEN if did_pass else bcolors.FAIL
    if did_pass:
        print(color + "Test Passed" + bcolors.ENDC)
    else:
        print(color + "Test Failed" + bcolors.ENDC)
        print(color + "Input: " + str(input) + " Expected Output: " + str(expected_output) + " Output: " + str(function(input)) + bcolors.ENDC)

def run_tests():
    print("Running tests...")

    # Test for print_hello
    print("Test 1: print_hello")
    print_hello("Alice")
    print()

    print("Test 2: find_closest_to_zero")
    test(find_closest_to_zero, [1, 2, 3, 4, 5], 1)
    test(find_closest_to_zero, [-1, -2, -3, -4, -5], -1)
    test(find_closest_to_zero, [2, -2, 3, -4, 5], 2)
    test(find_closest_to_zero, [0, -1], 0)
    print("Test 2: find_closest_to_zero completed \n")

    print("Test 3: number_vowels")
    test(number_vowels, "world", 1)
    test(number_vowels, "aeiou", 5)
    test(number_vowels, "bcdfgph", 0)
    test(number_vowels, "hello there", 4)
    print("Test 3: number_vowels completed \n")

    print("Test 4: sum_corners")
    test(sum_corners, [[1, 2], [4, 5]], 12)
    test(sum_corners, [[3, 8, 1], [7, 2, 4], [5, 9, 6]], 15)
    test(sum_corners, [[1, 1, 1 ], [1, 1, 1], [1, 1, 1]], 4)
    test(sum_corners, [[-4, -3, -2], [-1, 0, 1], [0, 3, 4]], -2)
    print("Test 4: sum_corners completed \n")

    print("Test 5: flip_matrix")
    test(flip_matrix, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    test(flip_matrix, [[1, 0, 1], [0, 1, 0], [1, 0, 1]], [[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    test(flip_matrix, [[1, 1, 0, 0], [0, 1, 1, 0]], [[0, 0, 1, 1], [1, 0, 0, 1]])
    print("Test 5: flip_matrix completed \n")

    print("Test 6: drawZ")
    test(drawZ, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [0, 1, 0], [1, 1, 1]])
    test(drawZ, [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], [[1, 1, 1, 1, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1]])
    print("Test 6: drawZ completed \n")

    print("Test 7: answerQuestion")
    test(answerQuestion, "How far away is the moon?", "238,855 miles")
    test(answerQuestion, "How far is the moon?", "238,855 miles")
    test(answerQuestion, "Is the sun very far?", -1)
    test(answerQuestion, "How big is the universe?", -1)
    print("Test 7: answerQuestion completed \n")

run_tests()