# Problem: Ice Cream Parlor
# Source: https://www.hackerrank.com/challenges/icecream-parlor/problem
# Topic: Search, Hash Table

def icecream_parlor(m, arr):
    # stores cost -> 1-based index
    seen = {}
    for idx, cost in enumerate(arr, 1):
        target = m - cost
        if target in seen:
            return [seen[target], idx]
        seen[cost] = idx
    return []
