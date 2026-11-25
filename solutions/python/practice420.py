# Problem: Remove the parentheses
# Source: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8
# Note: Removes parenthesized text, including nested groups.
# Status: Done


def remove_parentheses(st):
    result = []
    depth = 0

    for char in st:
        if char == "(":
            depth += 1
        elif char == ")":
            if depth > 0:
                depth -= 1
        elif depth == 0:
            result.append(char)

    return "".join(result)
