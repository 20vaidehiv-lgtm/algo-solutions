# Problem: Valid Parentheses
# Source: https://leetcode.com/problems/valid-parentheses/
# Note: Use a stack to match each closing bracket with the latest unmatched opening bracket
# Time: O(n), Space: O(n)

def is_valid(s):
    matching_open = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in matching_open:
            if not stack or stack.pop() != matching_open[char]:
                return False
        else:
            stack.append(char)

    return not stack
