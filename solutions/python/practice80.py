# Problem: Check if All Arrays Have Same Elements
# Source: 
# Note: Solves the Check if All Arrays Have Same Elements problem
# Description:
# Given a list of arrays, determine if all arrays contain the same elements (regardless of order).
# The function should return True if all arrays have the same elements, False otherwise.
# 
# Example:
# - Input: [[1,2,3], [3,1,2], [2,3,1]] → Output: True (all arrays have same elements)
# - Input: [[1,2,3], [3,1,2], [2,3,4]] → Output: False (last array has different element)
# 
# Status: ✅ SOLVED

def sol(arr):
    if not arr:
        return True
    
    l = sorted(arr[0])
    for i in arr[1:]:
        if sorted(i) != l:
            return False
    return True
