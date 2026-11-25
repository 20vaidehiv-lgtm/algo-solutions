# Problem: Palindrome Number
# Source: https://leetcode.com/problems/palindrome-number/


def is_palindrome(value):
    if isinstance(value, bool):
        return False

    try:
        number = int(value)
    except (TypeError, ValueError):
        return False

    text = str(number)
    return text == text[::-1]


if __name__ == "__main__":
    value = int(input())
    print("Palindrome" if is_palindrome(value) else "Not Palindrome")
