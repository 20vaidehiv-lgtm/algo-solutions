# Problem: String Jump Decoder
# Source: 
# Note: Decodes string by extracting characters at even indices
# 
# Description:
# Given a string where even-indexed characters are letters and odd-indexed characters are digits,
# decode the string by taking characters at even indices.
# 
# Status: ✅ SOLVED

def string_jump_decoder(s):
    if not s:
        return ""
    return s[::2]
