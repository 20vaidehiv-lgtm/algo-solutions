# Problem: Tribonacci Sequence
# Source: https://www.codewars.com/kata/556deca17c460c907e00000a
# Topic: Sequences, Math

def tribonacci(signature, n):
    if n <= 0:
        return []
    if n <= 3:
        return signature[:n]

    res = list(signature)
    for _ in range(n - 3):
        res.append(res[-1] + res[-2] + res[-3])
    return res
