import sys

sys.setrecursionlimit(10**6)
n = int(input())
a = list(map(int, input().split()))
memo = [[-1] * (n) for _ in range(n)]


def dp(i, j, memo):
    if i == j:
        return a[i]
    if memo[i][j] != -1:
        return memo[i][j]
    # take max of Lth vs Rth
    ans = max(a[i] - dp(i + 1, j, memo), a[j] - dp(i, j - 1, memo))
    memo[i][j] = ans
    return ans


diffr = dp(0, n - 1, memo)  # s1-s2
sm = sum(a)  # s1+s2
res = (sm + diffr) / 2  # s1
print(int(res))
