# Problem: Non-unique Elements
# Source: https://py.checkio.org/en/mission/non-unique-elements/
# Note: Removes elements that occur only once while preserving the original order.
# Description:
# Given an array of integers, return a new array containing only the elements that 
# appear more than once in the original array. The order of elements should be preserved.
#
# Input:
# - An array of integers `data`
#
# Output:
# - An array containing only the non-unique elements in their original order
#
# Status: ✅ SOLVED

from collections.abc import Iterable

def checkio(data: list[int]) -> Iterable[int]:
    unique = set(data)
    result = []
    for item in unique:
        if data.count(item) == 1:
            result.append(item)
    return [x for x in data if x not in result]

# Test cases with assertions
print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

#These "asserts" are used for self-checking
