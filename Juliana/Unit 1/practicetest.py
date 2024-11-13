from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
PART 1 GENERAL PYTHON PROGRAMMING
"""
# Question 1: ( 2 points ) Print Goodbye <name> 
# For example, if name is "Bob", the function should print "Goodbye Bob"
def print_goodbye(name):
    # TODO: Implement this function
    print("goodbye", name)


# Question 2: ( 2 points ) Given a string s, count the number of consonants (non-vowels) in the string.
def number_consonants(s):
    # TODO: Implement this function
    consonants = 'bcdfghjklmnpqrstvwxyz'
    punctuation = '!'
    count = 0
    for i in s.lower():
        if i in consonants:
            count = count + 1
    return count




# Question 3: ( 4 points ) Given a list of numbers, return the number farthest from zero.
# If there are two numbers equally far from zero, return the smaller one.
# You may NOT use the built-in abs function, but you can write your own.
def find_farthest_from_zero(numbers):
    # TODO: Implement this function
    farthest = numbers[0]
    for nums in numbers:
        abs = nums
        if nums < 0:
            nums = 0 - nums
        if nums > farthest:
            farthest = abs
    return farthest


"""
PART 2 MATRIX MANIPULATION
"""
# Question 4: ( 2 points ) Given a nxn matrix with at least 3 rows and 3 columns, return the sum of the four middle elements 
# (the elements adjacent to the center) in the matrix. Assume n is always odd.
def sum_middle_elements(matrix):
    # TODO: Implement this function
    sum = 0
    center = len(matrix)//2
    sum = matrix[center+1][center] + matrix[center-1][center] + matrix[center][center+1] + matrix[center][center-1]
    return sum


# Question 5: ( 4 points ) Given an nxm matrix, increment each element by 1 if it is even, and decrement by 1 if it is odd.
def modify_matrix(matrix):
    # TODO: Implement this function
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]%2 == 0:
                matrix[i][j] = matrix[i][j] + 1
            else:
                matrix[i][j] = matrix[i][j] - 1
    return matrix


# Question 6: ( 4 points ) Given an nxn (where n is odd) square matrix filled with 0s, return a matrix with a diagonal X pattern
# where both diagonals are filled with 1s.
def drawX(matrix):
    # TODO: Implement this function
    for i in range(len(matrix)):
        matrix[i][i] = 1
        matrix[i][(len(matrix))-i-1] = 1
    return matrix
        
            


"""
PART 3 COSINE SIMILARITY
"""

# Question 7: ( 2 points ) Using the function calculateCosineSimilarity, write a function similarQuestion 
# that checks if the cosine similarity between the user's question and the question "What is the capital of France?" 
# is at least 0.5. Return "Paris" if true, otherwise return -1.

# Given two strings, this function calculates the cosine similarity between the two strings
def calculateCosineSimilarity(string1, string2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([string1, string2])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

question = "What is the capital of France?"
answer = "Paris"

# Return answer if similarity >= 0.5, otherwise return -1.
def similarQuestion(userQuestion):
    #TODO: Implement this function
    similarity = calculateCosineSimilarity(userQuestion, question)  # Calculate similarity
    if similarity >= 0.5:
        return answer  # Return the predefined answer if similarity is above 0.5
    return -1  # Return -1 if similarity is less than 0.5



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

    # Test for print_goodbye
    print("Test 1: print_goodbye")
    print_goodbye("Bob")
    print()

    print("Test 2: find_farthest_from_zero")
    test(find_farthest_from_zero, [1, 2, 3, 4, 5], 5)
    test(find_farthest_from_zero, [-1, -2, -3, -4, -5], -5)
    test(find_farthest_from_zero, [2, -2, 3, -4, 5], -4)
    test(find_farthest_from_zero, [0, 1, -1], -1)
    print("Test 2: find_farthest_from_zero completed \n")

    print("Test 3: number_consonants")
    test(number_consonants, "hello", 3)
    test(number_consonants, "world", 4)
    test(number_consonants, "aeiou", 0)
    test(number_consonants, "python rocks!", 8)
    print("Test 3: number_consonants completed \n")

    print("Test 4: sum_middle_elements")
    test(sum_middle_elements, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 18)
    test(sum_middle_elements, [[3, 8, 1], [7, 2, 4], [5, 9, 6]], 20)
    print("Test 4: sum_middle_elements completed \n")

    print("Test 5: modify_matrix")
    test(modify_matrix, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 3, 2], [5, 4, 7], [6, 9, 8]])
    test(modify_matrix, [[0, 1], [2, 3]], [[1, 0], [3, 2]])
    print("Test 5: modify_matrix completed \n")

    print("Test 6: drawX")
    test(drawX, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    test(drawX, [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
    print("Test 6: drawX completed \n")

    print("Test 7: similarQuestion")
    test(similarQuestion, "What is the capital of France?", "Paris")
    test(similarQuestion, "Where is France's capital?", "Paris")
    test(similarQuestion, "What is the capital of Germany?", -1)
    test(similarQuestion, "How tall is the Eiffel Tower?", -1)
    print("Test 7: similarQuestion completed \n")

run_tests()