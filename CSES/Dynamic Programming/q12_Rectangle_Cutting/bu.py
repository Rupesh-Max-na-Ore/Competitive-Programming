a, b = map(int, input().split())

# dp[i][j] = min number of cuts to divide i x j rectangle into squares
dp = [[0] * (b + 1) for _ in range(a + 1)]

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if i == j:
            dp[i][j] = 0  # already a square, no cut needed
        else:
            min_cuts = float("inf")
            # try all vertical cuts
            for k in range(1, i):
                min_cuts = min(min_cuts, 1 + dp[k][j] + dp[i - k][j])
            # try all horizontal cuts
            for k in range(1, j):
                min_cuts = min(min_cuts, 1 + dp[i][k] + dp[i][j - k])
            dp[i][j] = min_cuts

print(dp[a][b])

# Python TLE even here. Java and cpp accepted.
