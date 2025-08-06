# n = int(input())
# total = n * (n + 1) // 2

# if total % 2 != 0:
#     print(0)
#     exit()

# target = total // 2

# dp = [[0] * (target + 1) for _ in range(n + 2)]

# # base
# dp[n + 1][target] = 1

# # recurr

# for i in range(n, 0, -1):
#     for j in range(0, target - i + 1):
#         dp[i][j] = dp[i + 1][j] + (dp[i + 1][j + i] if (j + i) <= target else 0)

# print(dp[1][0])

MOD = 10**9 + 7
n = int(input())
total = n * (n + 1) // 2

if total % 2 != 0:
    print(0)
    exit()

target = total // 2

dp = [[0] * (target + 1) for _ in range(n + 2)]
dp[n + 1][target] = 1  # base case

for i in range(n, 0, -1):
    for j in range(0, target + 1):
        dp[i][j] = dp[i + 1][j]
        if j + i <= target:
            dp[i][j] += dp[i + 1][j + i]

print((dp[1][0] // 2) % MOD)

# Still TLE on python, java solution is accepted
