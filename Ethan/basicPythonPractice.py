# Name:
# Date:
# Machine Learning Foundations
# Assingment 0_1 Python Coding Practice

# Function 1: Print Hello World
def print_hello_world():
    # TODO: Print "Hello, World!" to the console
    pass

# Function 2: Sum of Two Numbers
def sum_two_numbers(a, b):
    # TODO: Return the sum of a and b
    pass

# Function 3: Check if a List Contains an Element
def contains_element(lst, element):
    # TODO: Return True if element is in lst, otherwise False
    pass

# Function 4: Count Occurrences of a Character in a String
def count_char_in_string(s, char):
    # TODO: Return the number of times char appears in s
    pass

# Function 5: Create a List of Even Numbers
def list_even_numbers(n):
    # TODO: Return a list of even numbers from 0 to n-1
    pass

# Function 6: Find the Maximum Number in a List
def find_max(lst):
    # TODO: Return the maximum number in the list lst
    pass


# DO NOT MODIFY THE CODE BELOW
# Tests to check if the functions are implemented correctly
def run_tests():
    print("Running tests...")
    
    # Test for print_hello_world (manual observation needed)
    print("Test 1: print_hello_world")
    print_hello_world()
    print()
    
    # Test for sum_two_numbers
    print("Test 2: return sum")
    assert sum_two_numbers(3, 5) == 8
    assert sum_two_numbers(-1, 1) == 0
    assert sum_two_numbers(0, 0) == 0
    print("Test 2: sum_two_numbers passed")
    
    # Test for contains_element
    assert contains_element([1, 2, 3], 2) == True
    assert contains_element([1, 2, 3], 4) == False
    assert contains_element([], 1) == False
    print("Test 3: contains_element passed")
    
    # Test for count_char_in_string
    assert count_char_in_string("hello", "l") == 2
    assert count_char_in_string("world", "o") == 1
    assert count_char_in_string("", "a") == 0
    print("Test 4: count_char_in_string passed")
    
    # Test for list_even_numbers
    assert list_even_numbers(10) == [0, 2, 4, 6, 8]
    assert list_even_numbers(0) == []
    assert list_even_numbers(1) == [0]
    print("Test 5: list_even_numbers passed")
    
    # Test for find_max
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([0]) == 0
    print("Test 6: find_max passed")
    
    print("All tests passed!")

# Run the tests
run_tests()
