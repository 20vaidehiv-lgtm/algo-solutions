# Problem: Backspace String Compare
# Source: https://leetcode.com/problems/backspace-string-compare/
# Note: Solves the Backspace String Compare problem
# Description:
# Given two strings s and t, return true if they are equal when both are typed into 
# empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
#
# Input:
# - Two strings `s` and `t` containing lowercase letters and '#' characters
#
# Output:
# - A boolean indicating whether the strings are equal after processing backspaces
#
# Status: ✅ SOLVED

def backspaceStringCompare(s, t):
    def processString(string):
        result = []
        for char in string:
            if char != "#":
                result.append(char)
            elif result:
                result.pop()
        return result
    
    s_processed = processString(s)
    t_processed = processString(t)
    
    return s_processed == t_processed

# Test cases with assertions
# Example 1
s1, t1 = "ab#c", "ad#c"

# Example 2
s2, t2 = "ab##", "c#d#"

# Example 3
s3, t3 = "a#c", "b"

# Example 4
s4, t4 = "y#fo##f", "y#f#o##f"

# Example 5
s5, t5 = "a##c", "#a#c"

# Edge cases
s6, t6 = "", ""

s7, t7 = "###", "###"
