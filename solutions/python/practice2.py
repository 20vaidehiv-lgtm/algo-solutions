# Problem: Maximum Subarray
# Source: https://leetcode.com/problems/maximum-subarray/
# Note: Use Kadane's algorithm to track the best sum ending at each element
# Time: O(n), Space: O(n) because nums[1:] creates a copy
# Topic: arrays, dp
# Description:
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# A subarray is a contiguous part of an array.
#
# Input:
# - nums: An integer array where 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# Output:
# - An integer representing the maximum subarray sum
#
# Status: ✅ SOLVED

def maxSubArray(nums):
    """Return the maximum sum of a contiguous subarray in nums."""
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum





# All-zero input

# Zero is better than any negative element

# Positive elements separated by a loss cannot be combined arbitrarily

# The best subarray ends before a large trailing loss

# Maximum allowed length and element value
