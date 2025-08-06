n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

# i goes from n-1 to 0
for i in range(n - 1, -1, -1):
    for prev in range(i - 1, -2, -1):  # prev from i-1 to -1
        not_pick = dp[i + 1][prev + 1]
        pick = 0
        if prev == -1 or arr[i] > arr[prev]:
            pick = 1 + dp[i + 1][i + 1]
        dp[i][prev + 1] = max(pick, not_pick)

print(dp[0][0])

# for i in range(n):
#     print(dp[i])

# same as normal bu, just diffr indexing way
