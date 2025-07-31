import sys

sys.setrecursionlimit(10**6)


n = int(input())


# No need to actually keep set, just track sum
def fn(i, s1, s2):
    if i == n + 1:
        return 1 if s1 == s2 else 0

    return fn(i + 1, s1 + i, s2) + fn(i + 1, s1, s2 + i)


print(fn(1, 0, 0) // 2)
