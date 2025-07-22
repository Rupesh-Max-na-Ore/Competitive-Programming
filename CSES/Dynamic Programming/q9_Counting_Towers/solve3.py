MOD = 10**9 + 7


def solve(n):
    dp = [[0, 0] for _ in range(n + 2)]
    dp[1][0] = 1  # Fully filled tower of height 1
    dp[1][1] = 1  # Partial fill (gap)

    for i in range(2, n + 1):
        dp[i][0] = (dp[i - 1][0] * 4 + dp[i - 1][1]) % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * 2) % MOD

    return (dp[n][0] + dp[n][1]) % MOD


t = int(input())
a = []
for _ in range(t):
    n = int(input())
    a.append(solve(n))


for i in range(t):
    print(a[i])
