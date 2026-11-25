# Problem: Count Numbers with Even Number of Digits
# Source: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Note: Solves the Count Numbers with Even Number of Digits problem
# Description:
# Given a list of numbers, count how many of them have an even number of digits.
# A number has an even number of digits if the count of its digits is divisible by 2.
#
# Input:
# - An integer n representing the number of numbers to check
# - n lines of integers to check
#
# Output:
# - An integer representing the count of numbers with even number of digits
#
# Status: ✅ SOLVED

import math

# def evenNumberDigits(numbers):
#     if not numbers:
#         return 0
        
#     count = 0
#     for num in numbers:
#         if num == 0:
#             num_count = 1  # 0 has 1 digit
#         else:
#             num_count = math.floor(math.log10(abs(num))) + 1
            
#         if num_count % 2 == 0:
#             count += 1
#     return count

def evenNumberDigits(n):
    return sum(1 for num in n if len(str(num)) % 2 == 0)

# Test cases with assertions
# Example 1
numbers1 = [12, 345, 2, 6, 7896]

# Example 2
numbers2 = [555, 901, 482, 1771]

# Example 3
numbers3 = [1, 2, 3, 4, 5]

# Example 4
numbers4 = [10, 1000, 100000]

# Edge cases
numbers5 = []

numbers6 = [0]
