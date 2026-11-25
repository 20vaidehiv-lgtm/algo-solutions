# Problem: N-Queens II (count solutions)
# Source: https://leetcode.com/problems/n-queens-ii/
# Topic: Recursion, Backtracking
#
# Goal:
# Count how many ways N queens can be placed on an N x N chessboard
# so that no two queens attack each other (no shared row, column, or diagonal).
# We only need the number of ways, not the arrangements themselves.
#
# Idea (in plain words):
# Fill the board one row at a time. In each row, try every column and keep
# only the spots that are safe from the queens already placed, then move on
# to the next row. If no column in a row is safe, go back (backtrack) to the
# previous row and try a different spot there. Every time we manage to place
# a queen in the last row, we found one valid way, so we add 1 to the count.
#
# Why backtracking?
# Instead of listing every possible layout and checking it afterwards, we
# abandon a path as soon as it becomes invalid, which skips a lot of wasted work.
#
# Input:
# - n: size of the board (1 <= n <= 9)
#
# Output:
# - The total number of distinct valid arrangements (an integer).
#
# Complexity:
# - Time: O(N!) in the worst case, since we may try many placements per row.
# - Space: O(N^2) for the board, plus the recursion stack.
#
def totalNQueens(n):
    """Return the number of ways to place n non-attacking queens on an n x n board."""
    def is_safe(board, row, col):
        # Check row
        for j in range(n):
            if board[row][j] == 'Q':
                return False

        # Check column
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # Check diagonal (top-left to bottom-right)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, n), range(col, n)):
            if board[i][j] == 'Q':
                return False

        # Check diagonal (top-right to bottom-left)
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(board, row):
        if row == n:
            nonlocal count
            count += 1
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

    count = 0
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return count



# Note: Counts valid boards using bitmasks instead of scanning a 2D board.
#
# Optimization for issue #274:
# The original practice1.py checks rows, columns, and diagonals by scanning
# the board for every candidate position. This version represents occupied
# columns and diagonals as integer bitmasks, so each candidate set is computed
# with bitwise operations. It also avoids allocating and mutating an N x N board.
#
# Complexity: O(number of explored search states), with O(N) recursion space.
# The search is still backtracking, but each state performs constant-time
# bitmask operations rather than O(N) board scans per candidate.

def totalNQueens(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    full_mask = (1 << n) - 1

    def backtrack(columns, diagonals_left, diagonals_right):
        if columns == full_mask:
            return 1

        available = full_mask & ~(columns | diagonals_left | diagonals_right)
        count = 0

        while available:
            position = available & -available
            available ^= position
            count += backtrack(
                columns | position,
                ((diagonals_left | position) << 1) & full_mask,
                (diagonals_right | position) >> 1,
            )

        return count

    return backtrack(0, 0, 0)

