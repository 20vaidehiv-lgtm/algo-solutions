# Problem: Rank Transform of an Array
# Source: https://leetcode.com/problems/rank-transform-of-an-array/
# Note: Used sorted index mapping to rank elements starting from 1
#
# Description:
# Given an array of integers, replace each element with its rank. The rank represents 
# how large the element is. The rank has the following rules:
# - Rank 1 is the smallest element
# - Rank 2 is the second smallest element
# - And so on...
# - Equal elements get the same rank
#
# Input:
# - An array of integers `arr`
#
# Output:
# - An array where each element is replaced by its rank
#
# Status: ✅ SOLVED

def rankTransformArray(arr):
    """Replace each array element with its rank while assigning equal values the same rank."""
    if not arr:
        return []
    
    # Create a list of (value, index) pairs
    indexed_arr = [(val, i) for i, val in enumerate(arr)]
    
    # Sort by value
    indexed_arr.sort(key=lambda x: x[0])
    
    # Assign ranks
    ranks = [0] * len(arr)
    rank = 1
    
    for i in range(len(indexed_arr)):
        if i > 0 and indexed_arr[i][0] != indexed_arr[i-1][0]:
            rank += 1
        ranks[indexed_arr[i][1]] = rank
    
    return ranks
