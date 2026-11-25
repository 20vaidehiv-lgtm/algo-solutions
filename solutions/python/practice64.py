# Problem: Longest Substring Without Repeating Characters
# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Note: Finds length of longest substring without repeating characters using sets
#
# Description:
# Given a string, find the length of the longest substring without repeating characters.
# 
# Example:
# - Input: "abcabcbb" → Output: 3 (substring "abc" has length 3)
# - Input: "bbbbb" → Output: 1 (substring "b" has length 1)
# - Input: "pwwkew" → Output: 3 (substring "wke" has length 3)
# 
# Status: ✅ SOLVED

def longest_substring_without_repeating(s):
    if not s:
        return 0
    
    max_length = 0
    for i in range(len(s)):
        seen = set()
        current_length = 0
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            current_length += 1
        max_length = max(max_length, current_length)
    
    return max_length
