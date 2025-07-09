def countWays(n, x, coins):
    MOD = 10**9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1  # base: 1 way to make sum 0

    for coin in coins:
        for s in range(coin, x + 1):
            dp[s] = (dp[s] + dp[s - coin]) % MOD

    return dp[x]

n, sum = map(int, input().split())
curr = list(map(int, input().split()))
print(countWays(n, sum, curr))