n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))
dp = [[-1 for _ in range(n + 1)] for _ in range(x + 1)]


def fn(x, i):
    if i == n:
        return 0
    if dp[x][i] != -1:
        return dp[x][i]
    incl = 0
    if x - prices[i] >= 0:
        incl = pages[i] + fn(x - prices[i], i + 1)
    excl = fn(x, i + 1)
    dp[x][i] = max(incl, excl)
    return dp[x][i]


print(fn(x, 0))
