# Problem: Minimum Number of Jumps
# Source: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
# Topic: Dynamic Programming, Greedy
# Status: ✅ Done

def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    curr_end = 0
    farthest = 0

    for i in range(n):
        farthest = max(farthest, i + arr[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
            if curr_end >= n - 1:
                break
        if i >= farthest:
            return -1

    return jumps
