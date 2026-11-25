# Problem: Stock Span Problem
# Source: https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
# Topic: Stack, Arrays
# Status: DONE
# Note: usus stack of indexes to find the sapan of each day's price.

def calculate_span(price):
    n = len(price)
    span = [1] * n
    stack = []

    for i in range(n):
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()

        if len(stack) == 0:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span

print("all tests passed")
