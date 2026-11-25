# Problem: Build Tower
# Source: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
# Topic: String, Formatting
# Status: ✅ Done

def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        spaces = " " * (n_floors - i - 1)
        stars = "*" * (2 * i + 1)
        tower.append(spaces + stars + spaces)
    return tower
