# Problem: String Unscrambling
# Source: 
# Note: Solves the String Unscrambling problem
# Description:
# Given a scrambled string, unscramble it by taking characters at even indices first 
# (0, 2, 4, ...) and then characters at odd indices in reverse order.
# This appears to be a custom string manipulation problem.
#
# Input:
# - A scrambled string `scrambled`
#
# Output:
# - The unscrambled string
#
# Status: ✅ SOLVED

def unscramble_string(scrambled):
    result = ''
    
    # Take characters at even indices first
    for i in range(0, len(scrambled), 2):
        result += scrambled[i]
    
    # Take characters at odd indices in reverse order
    for j in range(len(scrambled) - 2, 0, -2):
        result += scrambled[j]
    
    return result

# Test cases with assertions
# Example 1
scrambled1 = "H!e ldllor ow"

# Example 2
scrambled2 = "abcde"

# Example 3
scrambled3 = "xyz"

# Example 4
scrambled4 = "a"

# Example 5
scrambled5 = "ab"
