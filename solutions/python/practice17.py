# Problem: Palindrome Number
# Source: https://leetcode.com/problems/palindrome-number/
# Note: Solves the Palindrome Number problem
# Description:
# Given an integer x, return true if x is a palindrome, and false otherwise.
# An integer is a palindrome when it reads the same backward as forward.
#
# Input:
# - An integer `x` where -2^31 <= x <= 2^31 - 1
#
# Output:
# - A boolean indicating whether the number is a palindrome
#
# Status: ✅ SOLVED

def isPalindrome1(n):
    """Check whether an integer is a palindrome by reversing its digits."""
    if n < 0:
        return False
        
    extracted_n = []
    temp = n
    while temp > 0:
        extracted_n.append(temp % 10)
        temp //= 10
    return extracted_n == extracted_n[::-1]

def isPalindrome2(n):
    """Check whether an integer is a palindrome by comparing its string representation."""
    if n < 0:
        return False
        
    n_str = str(n)
    return n_str == n_str[::-1]
