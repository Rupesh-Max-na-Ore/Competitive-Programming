MOD = 10**9 + 7

def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to make sum 0

    for i in range(1, n + 1):
        for j in range(1, 7):  # Try each dice face
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % MOD

    return dp[n]

n = int(input())
print(solve(n))
