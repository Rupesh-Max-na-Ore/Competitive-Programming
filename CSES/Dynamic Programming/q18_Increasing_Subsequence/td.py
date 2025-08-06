import sys

sys.setrecursionlimit(10000000)

n = int(input())
arr = list(map(int, input().split()))


def solve(n, arr):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def fnc(i, par):
        if i == n:
            return 0

        if dp[i][par] != -1:
            return dp[i][par]

        pick, not_pick = 0, 0
        if par == -1 or arr[par] < arr[i]:
            pick = 1 + fnc(i + 1, i)

        not_pick = fnc(i + 1, par)

        dp[i][par] = max(pick, not_pick)
        return dp[i][par]

    print(fnc(0, -1))

    for i in range(n):
        print(dp[i])


solve(n, arr)
