# Problem: Longest Common Prefix
# Source: https://leetcode.com/problems/longest-common-prefix/
# Note: Solves the Longest Common Prefix problem
# Description:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Input:
# - An array of strings `strs` where 1 <= strs.length <= 200
# - Each string in strs consists of only lowercase English letters
# - 0 <= strs[i].length <= 200
#
# Output:
# - A string representing the longest common prefix
#
# Status: ✅ SOLVED

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    sample_word = strs[0]

    for word in strs[1:]:
        while sample_word and word[:len(sample_word)] != sample_word:
            sample_word = sample_word[:-1]
    return sample_word

# def longestCommonPrefix(lst):
#     common = ""

#     for i in range(len(min(lst))):
#         w = min(lst)[i]
#         add = False
#         for word in lst:
#             if word[i] != w:
#                 add = False
#                 break
#             add = True
#         if add:
#             common += w

#     return common
