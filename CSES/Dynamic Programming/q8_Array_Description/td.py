MOD = 10**9 + 7


def pathTraversal(i, prev, a, n, m, dp):
    if i == n:
        return 1

    if dp[i][prev + 1] != -1:
        return dp[i][prev + 1]

    cnt = 0
    if a[i] != 0:
        if prev == -1 or abs(prev - a[i]) <= 1:
            cnt = pathTraversal(i + 1, a[i], a, n, m, dp)
    else:
        for v in range(1, m + 1):
            if prev == -1 or abs(prev - v) <= 1:
                cnt = (cnt + pathTraversal(i + 1, v, a, n, m, dp)) % MOD

    dp[i][prev + 1] = cnt
    return cnt


n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1 for _ in range(m + 2)] for _ in range(n)]

print(pathTraversal(0, -1, a, n, m, dp))
