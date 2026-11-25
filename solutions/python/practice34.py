# Problem: Sort an array containing 0s, 1s and 2s
# Source: GeeksforGeeks, Sort an array of 0s, 1s and 2s
# Note: Sort the values in ascending order and cover edge cases with assertions.

def sort012(arr):
    res = []
    for i in range(3):
        res += [i] * arr.count(i)
    return res


print(sort012([0, 1, 2, 0, 1, 2]))
