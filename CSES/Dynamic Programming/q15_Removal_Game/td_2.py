import sys

sys.setrecursionlimit(10**6)
n = int(input())
a = list(map(int, input().split()))
dp = [[-1] * n for _ in range(n)]


def fn(l, r):
    if l == r:
        return a[l]
    if l + 1 == r:
        return max(a[l], a[r])
    if dp[l][r] != -1:
        return dp[l][r]
    ans = max(
        a[l] + min(fn(l + 2, r), fn(l + 1, r - 1)),
        a[r] + min(fn(l + 1, r - 1), fn(l, r - 2)),
    )
    dp[l][r] = ans
    return ans


print(fn(l=0, r=n - 1))
