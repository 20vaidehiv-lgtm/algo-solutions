# Problem: Count Capital Letters in String
# Source: 
# Note: Solves the Count Capital Letters in String problem
# Topic: strings
# Description:
# Given a string, count the number of capital letters (uppercase characters) in it.
# The count starts at 1 and increments for each capital letter found.
#
# Input:
# - A string `s` containing letters
#
# Output:
# - An integer representing the count of capital letters plus 1
#
# Status: ✅ SOLVED

# def countCapitalLetters(s):
#     if not s:
#         return 1
        
#     count = 1
#     for char in s:
#         if char.isupper():
#             count += 1
#     return count

def countCapitalLetters(s):
    """Return the count of uppercase letters in a string plus one."""
    return sum(1 for c in s if c.isupper()) + 1
