// Problem: Merge Intervals
// Source: https://leetcode.com/problems/merge-intervals/
// Topic: Arrays, Sorting
// Status: IN PROGRESS

function merge(intervals) {
  if (intervals.length <= 1) {
    return intervals;
  }

  intervals.sort((a, b) => a[0] - b[0]);
  const merged = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const current = intervals[i];
    const last = merged[merged.length - 1];

    if (current[0] <= last[1]) {
      last[1] = current[1];
    } else {
      merged.push(current);
    }
  }

  return merged;
}

