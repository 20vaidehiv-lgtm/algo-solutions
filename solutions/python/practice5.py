# Problem: Spiral Matrix
# Source: https://leetcode.com/problems/spiral-matrix/
# Note: Solves the Spiral Matrix problem
# Topic: arrays, simulation
# Description:
# Given an m x n matrix, return all elements of the matrix in spiral order.
# The spiral order starts from the top-left corner and goes clockwise.
#
# Input:
# - matrix: A 2D integer array where m == matrix.length and n == matrix[i].length
# - 1 <= m, n <= 10
# - -100 <= matrix[i][j] <= 100
#
# Output:
# - A list of integers representing the spiral order traversal
#
# Status: ✅ SOLVED

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """Return the matrix elements in clockwise spiral order."""
    if not matrix or not matrix[0]:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result
