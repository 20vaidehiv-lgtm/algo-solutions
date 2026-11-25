# Problem: Clear Digits
# Source: https://leetcode.com/problems/clear-digits/
# Note: Removes each digit and the closest remaining non-digit character to its left.
# Description:
# Given a string s, remove all digits from the string. When a digit is encountered, 
# remove the character that comes before it as well.
# This appears to be a custom string manipulation problem.
#
# Input:
# - A string `s` containing letters and digits
#
# Output:
# - A string with digits and their preceding characters removed
#
# Status: ✅ SOLVED

# def clearDigits(s):
#     if not s:
#         return ""
        
#     result = []
#     for char in s:
#         if char.isdigit():
#             if result:  # Only pop if there's something to pop
#                 result.pop()
#         else:
#             result.append(char)

#     return ''.join(result)

def clearDigits(s):
    arr = []

    for c in s:
        if arr and c.isdigit():
            arr.pop()
        elif not c.isdigit():
            arr.append(c)
            
    return ''.join(arr)
