def minimize_coins(n, x, coins):
    INF = int(1e9)
    dp = [INF] * (x + 1)
    dp[0] = 0  # base case

    for i in range(1, x + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[x] if dp[x] != INF else -1


n, x = map(int, input().split())
curr = list(map(int, input().split()))
res = minimize_coins(n, x, curr)
print(res if res < int(1e9) else -1)