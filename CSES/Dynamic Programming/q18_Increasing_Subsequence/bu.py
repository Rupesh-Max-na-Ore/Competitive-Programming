n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    for par in range(0, i + 1):
        pick = 0
        not_pick = dp[i + 1][par]
        if par == 0 or arr[i] > arr[par - 1]:
            # pick = 1 + dp[i + 1][i] is wrong
            pick = 1 + dp[i + 1][i + 1]
        dp[i][par] = max(pick, not_pick)

# print(max(dp[0]))

# for i in range(n):
#     print(dp[i])

print(dp[0][0])
