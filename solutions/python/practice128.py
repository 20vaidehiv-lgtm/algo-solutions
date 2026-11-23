# Problem: Length of Last Word
# Source: https://leetcode.com/problems/length-of-last-word/
# Note: Split the string on whitespace and return the length of the last word (O(n) time).

def get_length(s):
    """Return the length of the last whitespace-separated word."""
    return len(s.split()[-1])
    
print(get_length('Hello World'))
print(get_length('     fly me   to    the    mooon   '))
