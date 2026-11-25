# Problem: Permutation Sequence
# Source: https://leetcode.com/problems/permutation-sequence/

from itertools import permutations
def kth_permutation(n, k):
    perms = list(map("".join, permutations("".join(map(str, range(1, n + 1))))))
    return f'"{perms[k - 1]}"'

print(kth_permutation(3, 3))
print(kth_permutation(4, 9))
print(kth_permutation(3, 1))
