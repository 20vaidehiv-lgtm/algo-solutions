# Problem: Largest Prime Factor
# Source: https://projecteuler.net/problem=3
# Topic: Math, Number Theory
# Status: IN PROGRESS

def largest_prime_factor(n):
    while n % 2 == 0:
        n //= 2
        last_factor = 2

    last_factor = 1
    d = 3
    while d * d <= n:
        if n % d == 0:
            last_factor = d
            n //= d
        d += 2

    return n if n > 1 else last_factor
