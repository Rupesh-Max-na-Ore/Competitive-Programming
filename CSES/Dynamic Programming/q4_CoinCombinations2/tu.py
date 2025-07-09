def ways(i, s, coins, dp):
    if s == 0:
        return 1
    if i < 0 or s < 0:
        return 0
    if dp[i][s] != -1:
        return dp[i][s]

    # Exclude coin[i], move to i-1; or include it, stay at i
    dp[i][s] = ways(i - 1, s, coins, dp) + ways(i, s - coins[i], coins, dp)
    return dp[i][s]

n, sum_ = map(int, input().split())
curr = list(map(int, input().split()))
dp = [[-1] * (sum_ + 1) for _ in range(n)]
print(ways(n - 1, sum_, curr, dp))
