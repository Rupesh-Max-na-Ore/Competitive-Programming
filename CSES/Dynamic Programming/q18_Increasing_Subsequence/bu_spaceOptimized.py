n = int(input())
arr = list(map(int, input().split()))

# dp = [[0] * (n + 1) for _ in range(n + 1)]
prev = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    for par in range(i, -1, -1):  # go reverse
        pick = 0
        not_pick = prev[par]
        if par == 0 or arr[i] > arr[par - 1]:
            # pick = 1 + dp[i + 1][i] is wrong
            pick = 1 + prev[i + 1]
        prev[par] = max(pick, not_pick)

# print(max(dp[0]))

# for i in range(n):
#     print(dp[i])

print(prev[0])
