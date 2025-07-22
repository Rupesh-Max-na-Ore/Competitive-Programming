MOD = 10**9 + 7


def solve(n):
    if n == 1:
        return 2
    if n == 2:
        return 8

    dp = [[0] * 9 for _ in range(n + 1)]

    for i in range(1, 8):
        dp[1][i] = 1

    cset1 = {1, 3, 4, 5, 6}
    cset2 = {2, 7, 8}
    pset1 = {1, 2, 4, 5, 6}
    pset2 = {3, 7, 8}

    for i in range(2, n + 1):
        for j in range(1, 8):
            if j in cset1:
                for pnum1 in pset1:
                    dp[i][j] += dp[i - 1][pnum1]
                    dp[i][j] %= MOD
            else:
                for pnum2 in pset2:
                    dp[i][j] += dp[i - 1][pnum2]
                    dp[i][j] %= MOD

    return (dp[n][3] + dp[n][7]) % MOD


t = int(input())
a = []
for _ in range(t):
    d = solve(int(input()))
    a.append(d)

for i in range(t):
    print(a[i])
