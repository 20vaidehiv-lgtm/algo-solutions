# Problem: Character Percentage in String
# Source: https://leetcode.com/problems/percentage-of-letter-in-string/
# Note: Solves the Character Percentage in String problem
# Description:
# Given a string s and a character c, return the percentage of characters in s that equal c.
# The percentage is rounded down to the nearest integer.
#
# Input:
# - A string `s` where 1 <= s.length <= 100
# - A character `c` to count in the string
#
# Output:
# - An integer representing the percentage of characters equal to c
#
# Status: ✅ SOLVED

# def percentageString(s, c):
#     if not s:
#         return 0
        
#     count = s.count(c)
#     return int((count / len(s)) * 100)

def percentageString(s, c):
    if not s:
        return 0
    return int(s.count(c)/len(s) * 100)
