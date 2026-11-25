# Problem: The Speed of Letters
# Source: https://www.codewars.com/kata/5fc7caa854783c002196f2cb
# Note: Each letter is placed at index i + (ord(letter) - 65), padded with spaces

def speedify(st):
    res = [" "] * (len(st) + 25)

    for i, l in enumerate(st):
        space = i + ord(l) - 65
        res[space] = l

    return "".join(res).rstrip()
