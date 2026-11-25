# Problem: Count Triplets
# Source: https://www.hackerrank.com/challenges/count-triplets-1/problem
# Note: Count partial triplets waiting for each next value in one left-to-right pass
# Time: O(n) expected, Space: O(n)


def countTriplets(arr, r):
    """Count index triples i < j < k with arr[j] = arr[i]*r and arr[k] = arr[j]*r."""
    waiting_second = {}
    waiting_third = {}
    total = 0

    for value in arr:
        # Only earlier indices may contribute to a triplet ending here.
        total += waiting_third.get(value, 0)
        next_value = value * r

        # Extend earlier single values into pairs waiting for their third value.
        pairs = waiting_second.get(value, 0)
        if pairs:
            waiting_third[next_value] = waiting_third.get(next_value, 0) + pairs

        # Register this value last so r = 1 never reuses the current index.
        waiting_second[next_value] = waiting_second.get(next_value, 0) + 1

    return total
