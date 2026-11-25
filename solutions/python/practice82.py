# Problem: Pow(x, n)
# Source: https://leetcode.com/problems/powx-n/
# Note: Solves the Pow(x, n) problem
# Description:
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
# Input:
# - x: A double representing the base number
# - n: An integer representing the exponent
# - -100.0 < x < 100.0
# - -2^31 <= n <= 2^31-1
# - n is an integer
# - -10^4 <= x^n <= 10^4
#
# Output:
# - A double representing x^n
#
# Status: ✅ SOLVED

def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1
    current_product = x
    
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2
    
    return result
