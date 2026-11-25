# Problem: Sum of Digits / Digital Root
# Source: https://www.codewars.com/kata/541c8630095125aba6000c00
# Note: Repeatedly sums the digits of a number until a single digit remains.
# Description:
# Given a positive integer, repeatedly sum its digits until you get a single digit.
# This is also known as the digital root of a number.
# 
# Example:
# - Input: 38 → Output: 2 (3+8=11, 1+1=2)
# - Input: 999 → Output: 9 (9+9+9=27, 2+7=9)
# - Input: 12345 → Output: 6 (1+2+3+4+5=15, 1+5=6)
# 
# Status: ✅ SOLVED

import math

def sum_digits(num: int) -> int:
    if num < 10:
        return num
    
    while num >= 10:
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        num = digit_sum
    
    return num
