# Problem: Length of Last Word
# Source: https://leetcode.com/problems/length-of-last-word/
# Note: Solves the Length of Last Word problem
# Topic: strings
# Description:
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Input:
# - s: A string where 1 <= s.length <= 10^4
# - s consists of only English letters and spaces ' '
# - There will be at least one word in s
#
# Output:
# - An integer representing the length of the last word
#
# Status: ✅ SOLVED

def lengthOfLastWord(s: str) -> int:
    """Return the length of the final word in the string."""
    # Remove trailing spaces and split by spaces
    words = s.strip().split()
    
    if not words:
        return 0
    
    return len(words[-1])
