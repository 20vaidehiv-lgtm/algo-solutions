# Problem: Common Child
# Source: https://www.hackerrank.com/challenges/common-child/problem
# Topic: Dynamic Programming, String
# Status: ✅ Done

def common_child(s1, s2):
    # 2D LCS table, kept to two rolling rows to save memory.
    # prev[j] = LCS length of s1[:i-1] and s2[:j]
    m = len(s2)
    prev = [0] * (m + 1)

    for a in s1:
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if a == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr

    return prev[m]

assert common_child("HARRY", "SALLY") == 2
assert common_child("AA", "BB") == 0
assert common_child("SHINCHAN", "NOHARAAA") == 3
assert common_child("ABCDEF", "FBDAMN") == 2
