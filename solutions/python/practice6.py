# Problem: Jump Game
# Source: https://leetcode.com/problems/jump-game/
# Note: Solves the Jump Game problem
# Time: O(n), Space: O(1)
# Topic: arrays, greedy
# Description:
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
#
# Input:
# - nums: An integer array where 1 <= nums.length <= 10^4
# - 0 <= nums[i] <= 10^5
#
# Output:
# - A boolean indicating whether you can reach the last index
#
# Status: ✅ SOLVED

def canJump(nums):
    """Return True if you can reach the last index, or False otherwise."""
    if not nums:
        return False
    
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return True
