a, b = map(int, input().split())

# Memoization table
dp = [[-1] * (b + 1) for _ in range(a + 1)]


def fnc(x, y):
    if x == y:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]

    res = float("inf")

    # Horizontal cuts
    for i in range(1, x):
        res = min(res, 1 + fnc(i, y) + fnc(x - i, y))

    # Vertical cuts
    for j in range(1, y):
        res = min(res, 1 + fnc(x, j) + fnc(x, y - j))

    dp[x][y] = res
    return res


print(fnc(a, b))
