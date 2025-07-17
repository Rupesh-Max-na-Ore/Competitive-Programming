def fn(x, y, a, dp):
    # base case
    if x == 0 and y == 0:
        return 1
    # Memoized case
    if dp[x][y] != -1:
        return dp[x][y]
    #  recurring case
    res = 0
    res += fn(x - 1, y, a, dp) if x - 1 >= 0 and a[x - 1][y] != "*" else 0
    res += fn(x, y - 1, a, dp) if y - 1 >= 0 and a[x][y - 1] != "*" else 0
    dp[x][y] = res
    return res


n = int(input())
a = [list(input().strip()) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
res = fn(n - 1, n - 1, a, dp)
print(res)
