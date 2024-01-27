# Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

# Example



# The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

# Function Description

# Complete the solve function in the editor below.

# solve has the following parameters:

# int n: the number of candy jars
# int operations[m][3]: a 2-dimensional array of operations
# Returns

# int: the floor of the average number of canidies in all jars
# Input Format

# The first line contains two integers,  and , separated by a single space.
#  lines follow. Each of them contains three integers, , , and , separated by spaces.

# Constraints





# Sample Input

# STDIN       Function
# -----       --------
# 5 3         n = 5, operations[] size = 3
# 1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# 2 5 100
# 3 4 100
# Sample Output

# 160
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'solve' function below.
def solve(n, operations):
    total_candies = 0
    for operation in operations:
        a, b, k = operation  # Unpack operation values
        jars_affected = b - a + 1  # Calculate the number of jars involved
        candies_added = k * jars_affected  # Calculate the total candies added
        total_candies += candies_added  # Add to the overall total

    average = total_candies // n  # Calculate the floor of the average
    return average  # Return the integer result

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        print("Environment variable OUTPUT_PATH not set.")
        sys.exit(1)

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    if result is not None:  # Only write if a valid result was obtained
        fptr.write(str(result) + '\n')

    fptr.close()
