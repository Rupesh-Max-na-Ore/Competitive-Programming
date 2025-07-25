import sys

sys.setrecursionlimit(10**6)

from functools import lru_cache

n = int(input())
grid = [input().strip() for _ in range(n)]


@lru_cache(None)
def fnc(i, j):
    if i >= n or j >= n:
        return "~"
    if i == n - 1 and j == n - 1:
        return grid[i][j]

    return grid[i][j] + min(fnc(i + 1, j), fnc(i, j + 1))


print(fnc(0, 0))
