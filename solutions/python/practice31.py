# Problem: Generate Palindrome ASCII
# Source:
# Note: Generates ASCII palindromic bit-strings; falls back to a provably valid result

import random

start = 65  # 'A'
end = 90    # 'Z'


def generate_palindrome_ascii(min_chars: int = 16, max_chars: int = 30, max_attempts: int = 10_000) -> tuple:
    """
    Return (string, binary_length) where the concatenated 7-bit representations
    of the characters form a binary palindrome of length > 100.

    Strategy: take a random left half, mirror its bits, and check whether the
    full binary string re-chunks cleanly into characters in [start, end].
    'A' (65 = 1000001) is a 7-bit palindrome, so a string of all A's is
    guaranteed to work and is used as the fallback after max_attempts.
    """
    for _ in range(max_attempts):
        half_chars = random.randint(min_chars, max_chars)
        left_half = [chr(random.randint(start, end)) for _ in range(half_chars)]
        left_bin = ''.join(format(ord(c), '07b') for c in left_half)
        palindrome_bin = left_bin + left_bin[::-1]

        # Total bit length must be a multiple of 7 and > 100
        if len(palindrome_bin) % 7 != 0 or len(palindrome_bin) <= 100:
            continue

        chunks = [palindrome_bin[i:i + 7] for i in range(0, len(palindrome_bin), 7)]
        try:
            full_str = ''.join(chr(int(chunk, 2)) for chunk in chunks)
        except ValueError:
            continue

        if all(start <= ord(c) <= end for c in full_str):
            return full_str, len(palindrome_bin)

    # Deterministic fallback: 'A' = 1000001 is a 7-bit palindrome, so any run of
    # A's produces a bit-string that equals its own reverse.
    fallback_len = max(min_chars * 2, 16)  # >= 16 chars -> 224 bits
    fallback_str = 'A' * fallback_len
    fallback_bits = ''.join(format(ord(c), '07b') for c in fallback_str)
    return fallback_str, len(fallback_bits)


if __name__ == "__main__":
    s, binary_len = generate_palindrome_ascii()
    print("Generated string:", repr(s))
    print("Binary length:", binary_len)
    bits = ''.join(format(ord(c), '07b') for c in s)
    print("Is palindrome:", bits == bits[::-1])
