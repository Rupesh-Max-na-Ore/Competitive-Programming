n = int(input())
a = list(map(int, input().split()))
# dp[i][j] = max |s1 - s2| for current player choice in space[i to j]
dp = [[0] * (n) for _ in range(n)]

# Base: 1 elem: p1 picks it
for i in range(n):
    dp[i][i] = a[i]

# RR
for left in range(n - 2, -1, -1):
    for right in range(left + 1, n, +1):
        dp[left][right] = max(
            a[left] - dp[left + 1][right], a[right] - dp[left][right - 1]
        )


diffr = dp[0][n - 1]  # s1-s2
sm = sum(a)  # s1+s2
res = (sm + diffr) / 2  # s1
print(int(res))
