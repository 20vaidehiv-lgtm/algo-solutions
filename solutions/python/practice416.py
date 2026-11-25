# Problem: Second Largest Distinct Number
# Source: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def second_largest(values):
    distinct = sorted(set(values), reverse=True)
    return distinct[1]


if __name__ == "__main__":
    values = set(map(int, input().split(",")))
    print(second_largest(values))
