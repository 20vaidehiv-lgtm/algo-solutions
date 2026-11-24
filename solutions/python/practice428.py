# Problem: Decode Ways
# Source: https://leetcode.com/problems/decode-ways/
# Topic: Dynamic Programming, String
# Status: ✅ Done

def decode(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one way to decode
    
    # Check the first character
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    
    for i in range(2, n + 1):
        # Check single digit
        one_digit = int(s[i-1:i])
        if one_digit >= 1:
            dp[i] += dp[i-1]
        
        # Check two digits
        two_digits = int(s[i-2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]

assert decode("12") == 2
assert decode("226") == 3
assert decode("06") == 0
assert decode("0") == 0
