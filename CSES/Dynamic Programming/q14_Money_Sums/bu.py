n = int(input())
coins = list(map(int, input().split()))
max_sum = sum(coins)

dp = [[False] * (max_sum + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for s in range(max_sum + 1):
        if dp[i][s]:
            dp[i + 1][s] = True
            if s + coins[i] <= max_sum:
                dp[i + 1][s + coins[i]] = True

result = [s for s in range(1, max_sum + 1) if dp[n][s]]
print(len(result))
print(" ".join(map(str, result)))
