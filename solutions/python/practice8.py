# Problem: Insert Interval
# Source: https://leetcode.com/problems/insert-interval/
# Note: Solves the Insert Interval problem
# Topic: arrays, intervals
# Description:
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order
# by starti. You are also given an interval newInterval = [start, end] that represents the start
# and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by
# starti and intervals still does not have any overlapping intervals.
#
# Input:
# - intervals: A 2D integer array where 0 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= starti <= endi <= 10^5
# - newInterval: A list of 2 integers [start, end]
#
# Output:
# - A 2D integer array representing the intervals after insertion
#
# Status: ✅ SOLVED

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """Return the intervals after inserting and merging the new interval."""
    result = []
    i = 0
    
    # Add all intervals that come before newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    result.append(newInterval)
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result
