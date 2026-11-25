# Problem: Fibonacci Sequence Generator
# Source: 
# Note: Solves the Fibonacci Sequence Generator problem
# Description:
# Generate the first n Fibonacci numbers starting from 0 and 1.
# Each number in the sequence is the sum of the two preceding ones.
#
# Input:
# - An integer `n` representing the number of Fibonacci numbers to generate
#
# Output:
# - A list containing the first n Fibonacci numbers
#
# Status: ✅ SOLVED

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[i] + fib[i + 1])
    
    return fib
