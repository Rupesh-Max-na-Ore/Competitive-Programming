n = int(input())
grid = [input().strip() for _ in range(n)]


def fnc(n, grid):
    dp = [["~"] * (n + 1) for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == n - 1 and j == n - 1:
                dp[i][j] = grid[i][j]
                break
            dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


print(fnc(n, grid))

# Java and Python are not accepted on CSES due to TLE
