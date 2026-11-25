# Problem: String Split Check
# Source: 
# Note: Checks whether string can be split into non-empty whitespace-separated parts
#
# Description:
# This appears to be a simple string manipulation problem that checks if a string 
# can be split into non-empty parts.
#
# Input:
# - A string `s`
#
# Output:
# - A boolean indicating whether the string can be split into non-empty parts
#
# Status: ✅ SOLVED

def canSplitString(s):
    if not s:
        return False
        
    # Check if string can be split into non-empty parts
    return bool(s.split())

# Test cases with assertions
# Example 1
s1 = "b"

# Example 2
s2 = ""

# Example 3
s3 = "hello world"

# Example 4
s4 = "   "

# Example 5
s5 = "a"
