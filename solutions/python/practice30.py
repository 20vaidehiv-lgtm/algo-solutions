# Problem: Alternating Digit Sum
# Source: https://leetcode.com/problems/alternating-digit-sum/
# Note: Solves the Alternating Digit Sum problem
# Description:
# Given a positive integer n, return the alternating digit sum of n.
# The alternating digit sum is the sum of the digits where the sign alternates 
# starting with positive for the leftmost digit.
#
# Input:
# - A positive integer `n`
#
# Output:
# - An integer representing the alternating digit sum
#
# Status: ✅ SOLVED

import math

# def sumAlternatingDigit(n):
#     if n == 0:
#         return 0
        
#     digitNum = math.floor(math.log10(abs(n))) + 1
#     sign = 1

#     if digitNum % 2 == 0:
#        sign = -1

#     totalSum = []

#     while n > 0:
#         m = n % 10 * sign
#         totalSum.append(m)
#         n //= 10
#         sign *= -1

#     return sum(totalSum)

def sumAlternatingDigit(n):
    sign = -1
    if len(str(n)) % 2 != 0:
        sign *= -1
    total = []
    
    while n > 0:
        total.append((n % 10) * sign)
        n //= 10
        sign *= -1
    
    return sum(total)
