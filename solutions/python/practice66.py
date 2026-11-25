# Problem: Sum of Multiples
# Source: https://leetcode.com/problems/sum-multiples/
# Note: Solves the Sum of Multiples problem
# Description:
# Given a positive integer n, find the sum of all numbers from 1 to n that are multiples of 3, 5, or 7.
# 
# Example:
# - Input: n = 10 → Output: 3 + 5 + 6 + 7 + 9 + 10 = 40
# - Input: n = 20 → Output: sum of multiples of 3, 5, or 7 up to 20
# 
# Status: ✅ SOLVED

def sum_of_multiples(n):
    if n <= 0:
        return 0
    
    total_sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total_sum += i
    return total_sum
