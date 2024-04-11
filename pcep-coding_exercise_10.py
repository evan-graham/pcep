# Coding Exercise 10: Get Rid of Duplicates!
#
# Scenario:
#
# Write a function named unique. The function should accept one parameter, which is a list with any number of elements inside. The default value for the parameter should be an empty list ([]).
#
# The function should return a new list with all duplicate elements removed. The function should preserve the original order of elements.
#
# Example 1: for unique([1, 1, 4, 5, 1]), the output should be [1, 4, 5]
# Example 2: for unique(['Mark', 'Mark', 'John', 'Anne']), the output should be  ['Mark', 'John', 'Anne']

def unique(user_input=[]):
    input_list = []
    for value in user_input:
        if value not in input_list:
            input_list.append(value)
    return print(input_list)