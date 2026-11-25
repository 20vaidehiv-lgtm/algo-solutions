# Problem: Fibonacci Number
# Source: https://leetcode.com/problems/fibonacci-number/
# Note: Solves the Fibonacci Number problem
# Description:
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1.
# That is, F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2) for n > 1.
# Given n, calculate F(n).
#
# Input:
# - An integer `n` where 0 <= n <= 30
#
# Output:
# - An integer representing the nth Fibonacci number
#
# Status: ✅ SOLVED

class Solution1(object):
    def fib(self, n):
        if n <= 1:
            return n
            
        base_fib = [0, 1]
        right = 1

        while len(base_fib) <= n:
            base_fib.append(base_fib[right - 1] + base_fib[right])
            right += 1

        return base_fib[n]

class Solution2(object):
    def fib(self, n):
        if n <= 1:
            return n
            
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

# Test cases with assertions
sol1 = Solution1()
sol2 = Solution2()
