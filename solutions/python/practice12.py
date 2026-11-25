# Problem: Reverse String II
# Source: https://leetcode.com/problems/reverse-string-ii/
# Note: Solves the Reverse String II problem
# Time: O(n), Space: O(n)
# Description:
# Given a string s and an integer k, reverse the first k characters for every 2k characters 
# counting from the beginning of the string. If there are fewer than k characters left, 
# reverse all of them. If there are less than 2k but greater than or equal to k characters, 
# then reverse the first k characters and leave the other as original.
#
# Input:
# - A string `s` where 1 <= s.length <= 10^4
# - An integer `k` where 1 <= k <= 10^4
# - s consists of only lowercase English letters
#
# Output:
# - A string with the specified characters reversed
#
# Status: ✅ SOLVED

class Solution(object):
    def reverseStr(self, s, k):
        """Reverse the first k characters in every 2k characters of the given string."""
        s_list = list(s)
        n = len(s_list)
        
        for i in range(0, n, 2*k):
            # Reverse the first k characters
            left = i
            right = min(i + k - 1, n - 1)
            
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        return ''.join(s_list)

# Test cases with assertions
sol = Solution()
