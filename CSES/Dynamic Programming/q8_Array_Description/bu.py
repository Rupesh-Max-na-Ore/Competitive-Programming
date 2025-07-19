MOD = 10**9 + 7


def solve(n, m, a):
    # dp[i][prev_val] = number of ways to fill a[i:] if a[i-1] = prev_val
    dp = [[0] * (m + 2) for _ in range(n + 1)]

    # Base case: dp[n][*] = 1, since if we've filled the whole array, it's valid
    for prev in range(1, m + 1):
        dp[n][prev] = 1

    for i in range(n - 1, -1, -1):  # from n−1 down to 0
        for prev in range(1, m + 1):
            if a[i] != 0:
                if abs(a[i] - prev) <= 1:
                    dp[i][prev] = dp[i + 1][a[i]]
            else:
                for v in [prev - 1, prev, prev + 1]:
                    if 1 <= v <= m:
                        dp[i][prev] = (dp[i][prev] + dp[i + 1][v]) % MOD

    # At i=0, there's no prev value yet ⇒ try all possible initial values
    if a[0] != 0:
        return dp[1][a[0]]
    else:
        return sum(dp[1][v] for v in range(1, m + 1)) % MOD


n, m = map(int, input().split())
a = list(map(int, input().split()))

print(solve(n, m, a))
