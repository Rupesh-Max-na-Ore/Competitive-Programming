def fn(n, a):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            # Base case
            if x == 0 and y == 0:
                dp[x][y] = 1
            # Recursive case
            if x - 1 >= 0 and a[x - 1][y] != "*":
                dp[x][y] += dp[x - 1][y]
            if y - 1 >= 0 and a[x][y - 1] != "*":
                dp[x][y] += dp[x][y - 1]
    return dp[n - 1][n - 1]


n = int(input())
a = [list(input().strip()) for _ in range(n)]
print(fn(n, a))
