# Given a number N reverse the number and print it.

# Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

# Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

# Input Format

# 123

# Constraints

# N <= 1000

# Output Format

# 321


logic 1
N = input()
print(N[::-1])

logic 2

num = input()
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))