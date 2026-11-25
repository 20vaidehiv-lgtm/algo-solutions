# Problem: Sort Characters By Frequency
# Source: https://leetcode.com/problems/sort-characters-by-frequency/
# Note: Sorts characters in descending order of their frequency
# Note: Ties are ordered alphabetically.

from collections import Counter
def sort_characters_by_frequency(s):
    """Return string s with characters sorted by descending frequency and ascending alphabetical order."""

    freq = Counter(s)
    
    return ''.join(sorted(s, key=lambda c: (-freq[c], c)))


print(sort_characters_by_frequency('cbaba'))
