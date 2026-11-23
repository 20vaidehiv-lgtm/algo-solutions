# Problem: Koko Eating Bananas
# Source: https://leetcode.com/problems/koko-eating-bananas/
# Topic: Binary Search, Arrays
# Status: ✅ Done

def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        total_hours = sum((p + mid - 1) // mid for p in piles)

        if total_hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

assert min_eating_speed([3, 6, 7, 11], 8) == 4
assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
assert min_eating_speed([1], 1) == 1
assert min_eating_speed([1000000000], 2) == 500000000
