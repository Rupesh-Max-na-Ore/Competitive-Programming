n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = a[i]

for i in range(1, n):
    dp[i - 1][i] = max(a[i - 1], a[i])

# for i in range(n - 1):
#     dp[i][i + 1] = max(a[i], a[i + 1])

# Fill for lengths >= 3
for length in range(3, n + 1):  # length of subarray
    for l in range(
        n - length + 1
    ):  # l start n-2 only, [r-l] keeps increasing with length tracking it
        r = l + length - 1
        dp[l][r] = max(
            a[l]
            + min(
                dp[l + 2][r] if l + 2 <= r else 0,
                dp[l + 1][r - 1] if l + 1 <= r - 1 else 0,
            ),
            a[r]
            + min(
                dp[l + 1][r - 1] if l + 1 <= r - 1 else 0,
                dp[l][r - 2] if l <= r - 2 else 0,
            ),
        )

print(dp[0][n - 1])

# This solution TLE in python due to so many ifs
