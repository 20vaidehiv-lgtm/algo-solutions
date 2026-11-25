# Problem: Frequency Counter
# Source: 
# Note: Counts string frequencies and formats descending frequency output
#
# Description:
# Given a list of strings, count the frequency of each string and return a formatted result string
# showing each unique string and its count, sorted by frequency in descending order.
# 
# Example:
# - Input: ["a", "b", "a", "c", "b", "a"]
# - Output: "a - 3, b - 2, c - 1"
# 
# Status: ✅ SOLVED

def frequency_counter(strings):
    if not strings:
        return ""
    
    # Count frequencies
    freq = {}
    for s in strings:
        freq[s] = freq.get(s, 0) + 1
    
    # Sort by frequency (descending) and then by string (ascending for ties)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Format result
    result_parts = []
    for item, count in sorted_items:
        result_parts.append(f"{item} - {count}")
    
    return ", ".join(result_parts)
