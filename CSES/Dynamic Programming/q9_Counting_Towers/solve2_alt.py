MOD = 10**9 + 7

# Pre-allocate the DP table with size (1e6 + 1) × 2
N = 10**6 + 1
dp = [[0, 0] for _ in range(N)]

t = int(input())
for _ in range(t):
    n = int(input())

    # Base case initialization
    dp[n][0] = 1
    dp[n][1] = 1

    # Fill the table from i = n-1 down to 0
    for i in range(n - 1, -1, -1):
        dp[i][0] = (2 * dp[i + 1][0] + dp[i + 1][1]) % MOD
        dp[i][1] = (4 * dp[i + 1][1] + dp[i + 1][0]) % MOD

    # Output the result
    print((dp[1][0] + dp[1][1]) % MOD)
